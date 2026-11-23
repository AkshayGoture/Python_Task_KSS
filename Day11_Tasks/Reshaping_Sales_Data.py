import numpy as np

# Monthly sales data
sales = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

# Convert list into NumPy array
arr = np.array(sales)

# Reshape into 4 months × 3 products
reshaped_arr = arr.reshape(4, 3)

# Print the reshaped array
print("Sales Matrix:")
print(reshaped_arr)
