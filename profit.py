import time
import random

while True:
    # 1. Variables
    bitcoin_amount = 2.5
    buy_price = 100000
    current_price = random.randint(90000, 110000)

    # 2. Math Logic
    cost = bitcoin_amount * buy_price
    value_now = bitcoin_amount * current_price
    profit = value_now - cost

    # 3. Report
    print("--------------------------------")
    print(f"PRICE: ${current_price}")
    print(f"PROFIT: ${profit}")

    # 4. Trading Signal
    target_profit_rate = 10000

    if profit > target_profit_rate:
        print("SIGNAL: 🚀 MOONING! SELL SELL SELL!")
    elif profit < 0:
        print("SIGNAL: 🔻 LOSS! PANIC HOLD!")
    else:
        print("SIGNAL: 💤 Boring market. Holding.")

    time.sleep(2)
