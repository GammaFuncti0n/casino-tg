from telegram.ext import ApplicationBuilder
from config import BOT_TOKEN
from handlers.slot import get_spin_handler

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(get_spin_handler())
    app.run_polling()

if __name__ == "__main__":
    main()
