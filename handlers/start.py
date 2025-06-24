from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from services.wallet import get_balance

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    balance = get_balance(user_id)

    await update.message.reply_text(
        f"Добро пожаловать в слот-казино! 🎰\n"
        f"Ваш стартовый баланс: {balance} монет\n"
        f"Чтобы сыграть, отправьте команду: /spin <ставка>\n"
        f"Например: /spin 100"
    )

def get_start_handler():
    return CommandHandler("start", start)
