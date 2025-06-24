from telegram.ext import ApplicationBuilder
import yaml
from handlers.slot import get_spin_handler

def main():
    with open("credentials.yaml") as f:
        BOT_TOKEN = yaml.safe_load(f)['BOT_TOKEN']
    print(BOT_TOKEN)
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(get_spin_handler())
    app.run_polling()

if __name__ == "__main__":
    main()
