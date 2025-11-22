import requests

# 1. The Target URl 
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"


# 2. SEND the WAITER
print("Connecting to the internet...")
response = requests.get(url)


# 3. Check the Plate (The Data)
data = response.json()


# 4. Print the result
print("--- LIVE DATA ---")
print(data)


# 5. Dig out the price
price = data['bitcoin']['usd']
print(f"REAL BITCOIN PRICE: ${price}")
