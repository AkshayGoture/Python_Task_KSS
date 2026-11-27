# Product Sales Bar Chart 
#Scenario: products = ["Pen", "Book", "Pencil"] sales = np.array([50, 80, 40]) 
#Task: ● Create DataFrame ● Plot bar chart ● Add labels and title 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create product and sales data
products = ["Pen", "Book", "Pencil"]
sales = np.array([50, 80, 40])

# Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

# Display DataFrame
print(df)

# Plot bar chart
plt.bar(df["Product"], df["Sales"], color=["blue", "green", "orange"])

# Add labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Bar Chart")

# Display chart
plt.show()
