import random

SYMBOLS = ["🍒", "🍋", "🔔", "💎", "🍀", "⭐"]

def spin_slots():
    result = [random.choice(SYMBOLS) for _ in range(3)]
    if result[0] == result[1] == result[2]:
        multiplier = 10
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        multiplier = 2
    else:
        multiplier = 0
    return result, multiplier
