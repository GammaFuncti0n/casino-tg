import json
import os

WALLET_FILE = "data/wallets.json"
DEFAULT_BALANCE = 1000

def load_wallets():
    os.makedirs(os.path.dirname(WALLET_FILE), exist_ok=True)

    # если файл не существует или пустой — записываем {}
    if not os.path.exists(WALLET_FILE) or os.path.getsize(WALLET_FILE) == 0:
        with open(WALLET_FILE, "w") as f:
            json.dump({}, f)

    with open(WALLET_FILE, "r") as f:
        return json.load(f)

def save_wallets(wallets):
    with open(WALLET_FILE, "w") as f:
        json.dump(wallets, f, indent=4)

def get_balance(user_id):
    wallets = load_wallets()
    return wallets.get(str(user_id), DEFAULT_BALANCE)

def update_balance(user_id, new_balance):
    wallets = load_wallets()
    wallets[str(user_id)] = new_balance
    save_wallets(wallets)
