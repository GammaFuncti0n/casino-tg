from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from services.wallet import get_balance

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    balance = get_balance(user_id)
    await update.message.reply_text(f"Ваш текущий баланс: {balance} монет")

def get_balance_handler():
    return CommandHandler("balance", balance)