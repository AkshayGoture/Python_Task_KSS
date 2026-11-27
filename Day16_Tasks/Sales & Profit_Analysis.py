 #Product Sales & Profit Analysis 
#Scenario: sales = np.array([200, 300, 250, 400, 350]) profit = np.array([50, 70, 60, 90, 80]) products = ["A", "B", "C", "D", "E"] 
#Task: ● Create DataFrame ● Plot: 
#○ Line graph → sales trend ○ Bar chart → product vs sales ○ Pie chart → sales contribution ○ Histogram → profit distribution ○ Scatter plot → sales vs profit

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

# DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})
print(df)

# Graphs
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(products, sales, marker='o')
plt.title("Sales Trend")

plt.subplot(2, 3, 2)
plt.bar(products, sales, color='orange')
plt.title("Product vs Sales")

plt.subplot(2, 3, 3)
plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Sales Contribution")

plt.subplot(2, 3, 4)
plt.hist(profit, color='green', edgecolor='black')
plt.title("Profit Distribution")

plt.subplot(2, 3, 5)
plt.scatter(sales, profit, color='red')
plt.title("Sales vs Profit")

plt.tight_layout()
plt.show()

# Analysis
print("Total Sales:", sum(sales))
print("Total Profit:", sum(profit))
print("Average Sales:", np.mean(sales))
print("Average Profit:", np.mean(profit))
