#Expense Distribution Pie Chart 
#Scenario: Monthly expenses: expenses = np.array([500, 300, 200]) labels = ["Food", "Rent", "Travel"] 
#Task: ● Create a pie chart ● Show percentage distribution 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create expense data
expenses = np.array([500, 300, 200])
labels = ["Food", "Rent", "Travel"]

# Create DataFrame
df = pd.DataFrame({
    "Category": labels,
    "Expenses": expenses
})

# Display DataFrame
print(df)

# Create pie chart
plt.pie(
    expenses,
    labels=labels,
    autopct='%1.1f%%',
    colors=['orange', 'skyblue', 'lightgreen'],
    startangle=90
)

# Add title
plt.title("Monthly Expense Distribution")

# Display chart
plt.show()
