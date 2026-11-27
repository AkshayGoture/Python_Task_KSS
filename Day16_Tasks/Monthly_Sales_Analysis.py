# Monthly Sales Analysis 
#Scenario: sales = np.array([100, 150, 200, 180, 220, 300]) months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
#Task: ● Create DataFrame ● Plot: 
#○ Line graph → sales trend ○ Bar chart → month-wise comparison ○ Pie chart → contribution of each month ○ Histogram → frequency of sales values ○ Scatter plot → month index vs sales


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create DataFrame
df = pd.DataFrame({"Month": months, "Sales": sales})
print(df)

# Line Graph
plt.plot(months, sales, marker='o')
plt.title("Sales Trend")
plt.show()

# Bar Chart
plt.bar(months, sales, color='orange')
plt.title("Monthly Sales")
plt.show()

# Pie Chart
plt.pie(sales, labels=months, autopct='%1.1f%%')
plt.title("Sales Contribution")
plt.show()

# Histogram
plt.hist(sales, bins=5, color='green')
plt.title("Sales Frequency")
plt.show()

# Scatter Plot
plt.scatter(range(1, 7), sales, color='red')
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.show()
