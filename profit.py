import time
import requests # <--- The new connector



trade_history = []

buy_price = 96000   # We assume we bought at $96k

bitcoin_amount = 1.5 



print("🤖 BOT INITIALIZED. CONNECTING TO BINANCE/COINGECKO...")
while True:

    # 1. FETCHING THE REAL PRICE (The API Call)

    try:

        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

        response = requests.get(url)

        data = response.json()

        current_price = data['bitcoin']['usd'] # Extract the number

    except Exception as e:

        print("Connection Error... retrying.")

        time.sleep(5)

        continue



    # 2. MATHS LOGIC

    cost = bitcoin_amount * buy_price

    value_now = bitcoin_amount * current_price

    profit = value_now - cost

    

    # 3. SNIPPET FOR RECORDING HISTORY

    trade_history.append(profit)



    # 4. REPORT

    print("--------------------------------")

    print(f"LIVE PRICE : ${current_price}")

    print(f"YOUR PROFIT: ${profit}")

    print(f"LOG SIZE   : {len(trade_history)} checks")



    # 5. SIGNALS

    if profit > 5000:

        print("SIGNAL: 🚀 WE ARE IN PROFIT!")

    elif profit < 0:

        print("SIGNAL: 🔻 LOSS. HOLD THE LINE.")

    else:

        print("SIGNAL: 💤 Small movement.")



    # CRITICAL: Sleep for 30 seconds to avoid getting banned by the API

    # If you spam the server too fast, they will block your IP.

    print("Waiting 45s for next update...")
    time.sleep(45)
