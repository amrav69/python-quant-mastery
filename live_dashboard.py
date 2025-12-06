import matplotlib.pyplot as plt
import requests
import time

# 1. Setup the Empty Storage
prices = []
x_time = []
counter = 0

# 2. Setup the Graph Window
plt.ion() # Interactive Mode ON (Allows live updates)
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x_time, prices, 'b-') # Draw an empty blue line
plt.title("Live Bitcoin Price Feed")
plt.xlabel("Time (Ticks)")
plt.ylabel("Price (USD)")

print("Starting Live Feed... (Press Ctrl+C to stop)")

# 3. The Infinite Loop
while True:
    try:
        # A. Fetch Data
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        current_price = data['bitcoin']['usd']
        
        # B. Update Lists
        prices.append(current_price)
        x_time.append(counter)
        counter += 1
        
        # C. Update the Graph
        line1.set_xdata(x_time)
        line1.set_ydata(prices)
        
        # Adjust the camera (zoom to fit new data)
        ax.relim()
        ax.autoscale_view()
        
        # Draw and Pause
        # This draws the update and waits 2 seconds before looping
        plt.draw()
        plt.pause(2) 
        
        print(f"Tick {counter}: ${current_price}")

    except Exception as e:
        print("Error fetching data...")
        time.sleep(2)
