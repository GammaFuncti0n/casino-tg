from telegram.ext import ApplicationBuilder
import yaml
from handlers.slot import get_spin_handler
from handlers.start import get_start_handler
from handlers.balance import get_balance_handler

def main():
    with open("credentials.yaml") as f:
        BOT_TOKEN = yaml.safe_load(f)['BOT_TOKEN']
    print(BOT_TOKEN)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(get_start_handler())
    app.add_handler(get_balance_handler())
    app.add_handler(get_spin_handler())
    #app.add_handler(get_button_handler())
    app.run_polling()

if __name__ == "__main__":
    main()
