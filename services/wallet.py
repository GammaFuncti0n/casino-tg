import json
import os

WALLET_FILE = "data/wallets.json"
DEFAULT_BALANCE = 1000

def load_wallets():
    if not os.path.exists(WALLET_FILE):
        os.makedirs(os.path.dirname(WALLET_FILE), exist_ok=True)
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
