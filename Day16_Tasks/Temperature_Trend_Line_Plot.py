#Temperature Trend Line Plot 
#Scenario: Daily temperatures: temps = np.array([28, 30, 32, 31, 29]) 
#Task: ● Convert into Pandas Series ● Plot a line graph ● Add title and grid 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create temperature data
temps = np.array([28, 30, 32, 31, 29])

# Convert NumPy array into Pandas Series
temperature = pd.Series(temps)

# Display Series
print(temperature)

# Plot line graph
plt.plot(temperature, marker='o', color='blue', linestyle='-')

# Add title and labels
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Add grid
plt.grid(True)

# Display graph
plt.show()
