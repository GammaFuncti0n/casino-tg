from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from services.game_logic import spin_slots
from services.wallet import get_balance, update_balance

async def spin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args

    if len(args) != 1 or not args[0].isdigit():
        await update.message.reply_text("Используй: /spin <ставка>, например /spin 100")
        return

    bet = int(args[0])
    balance = get_balance(user_id)
    if bet <= 0:
        await update.message.reply_text(f"{bet} некорректная ставка")
        return
    
    if bet > balance:
        await update.message.reply_text(f"Недостаточно средств. Баланс: {balance} монет.")
        return

    slots, multiplier = spin_slots()
    result_str = " | ".join(slots)

    if multiplier > 0:
        winnings = bet * multiplier
        balance = balance - bet + winnings
        update_balance(user_id, balance)
        await update.message.reply_text(
            f"{result_str}\nПоздравляем! Выигрыш x{multiplier}: +{winnings} монет\nБаланс: {balance}"
        )
    else:
        balance -= bet
        update_balance(user_id, balance)
        await update.message.reply_text(
            f"{result_str}\nУвы, вы проиграли {bet} монет.\nБаланс: {balance}"
        )

def get_spin_handler():
    return CommandHandler("spin", spin)
