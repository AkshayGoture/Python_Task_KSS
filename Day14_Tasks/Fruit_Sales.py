#Fruit Sales Comparison (Series Addition) 
#A shop tracks fruit sales: S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"]) 
#Task: ● Add both series ● Find the total sales of all fruits combined

import pandas as pd

# Create two Series
S1 = pd.Series([10, 20, 30],
               index=["apple", "banana", "cherry"])

S2 = pd.Series([5, 15, 25],
               index=["apple", "banana", "cherry"])

# Add both Series
total = S1 + S2

# Calculate total sales of all fruits
total_sales = total.sum()

# Display results
print("Fruit-wise Total Sales:")
print(total)

print("\nTotal Sales of All Fruits:", total_sales)
