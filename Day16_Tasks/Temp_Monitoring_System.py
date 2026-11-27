# Temperature Monitoring System 
#Scenario: temps = np.array([28, 30, 32, 35, 33, 31, 29]) days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
#Task: ● Create DataFrame ● Plot: 
#○ Line graph → daily temperature trend ○ Bar chart → day-wise temperature ○ Pie chart → proportion of high (>30) vs low temps ○ Histogram → temperature frequency ○ Scatter plot → day index vs temperature
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# DataFrame
df = pd.DataFrame({"Day": days, "Temperature": temps})
print(df)

# High and Low Temperatures
high = sum(temps > 30)
low = sum(temps <= 30)

# Graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(days, temps, marker='o')
plt.title("Daily Temperature Trend")

plt.subplot(2, 3, 2)
plt.bar(days, temps, color='orange')
plt.title("Day-wise Temperature")

plt.subplot(2, 3, 3)
plt.pie([high, low], labels=["High", "Low"],
        autopct='%1.1f%%')
plt.title("High vs Low Temperature")

plt.subplot(2, 3, 4)
plt.hist(temps, bins=5, color='green', edgecolor='black')
plt.title("Temperature Frequency")

plt.subplot(2, 3, 5)
plt.scatter(range(len(temps)), temps, color='red')
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature")

plt.tight_layout()
plt.show()

# Analysis
print("Average Temperature:", np.mean(temps))
print("Maximum Temperature:", np.max(temps))
print("Minimum Temperature:", np.min(temps))
print("High Temperature Days:", high)
print("Low Temperature Days:", low)
