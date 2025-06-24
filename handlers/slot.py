from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from services.game_logic import spin_slots
from services.wallet import get_balance, update_balance

# Храним последние ставки пользователей
last_bets = {}

async def run_spin(user_id: int, bet: int, respond, silent=False):
    balance = get_balance(user_id)

    if bet <= 0:
        if not silent:
            await respond(f"{balance} некорректная ставка")
        return
    if bet > balance:
        if not silent:
            await respond(f"Недостаточно средств. Баланс: {balance} монет.")
        return

    slots, multiplier = spin_slots()
    result_str = " | ".join(slots)

    if multiplier > 0:
        winnings = bet * multiplier
        balance = balance - bet + winnings
        update_balance(user_id, balance)
        outcome = f"Поздравляем! Выигрыш x{multiplier}: +{winnings} монет"
    else:
        balance -= bet
        update_balance(user_id, balance)
        outcome = f"Увы, вы проиграли {bet} монет."

    last_bets[user_id] = bet  # обновим ставку

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔽 /2", callback_data="half"),
            InlineKeyboardButton("🔁 Повтор", callback_data="repeat"),
            InlineKeyboardButton("🔼 *2", callback_data="double"),
        ]
    ])

    await respond(f"{result_str}\n{outcome}\nБаланс: {balance}", reply_markup=keyboard)

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    if len(args) != 1 or not args[0].isdigit():
        await update.message.reply_text("Используй: /spin <ставка>, например /spin 100")
        return

    bet = int(args[0])
    await run_spin(user_id, bet, respond=update.message.reply_text)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    balance = get_balance(user_id)
    prev_bet = last_bets.get(user_id, 100)

    if query.data == "half":
        new_bet = max(1, prev_bet // 2)
    elif query.data == "repeat":
        new_bet = prev_bet
    elif query.data == "double":
        new_bet = prev_bet * 2
    else:
        return

    await run_spin(user_id, new_bet, respond=query.message.reply_text, silent=True)


def get_spin_handler():
    return CommandHandler("spin", spin)

def get_button_handler():
    return CallbackQueryHandler(handle_button)
