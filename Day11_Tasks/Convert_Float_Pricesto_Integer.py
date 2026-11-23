import numpy as np

# Product prices
prices = np.array([10.5, 20.8, 15.3])

# Convert float array to integer
integer_prices = prices.astype(int)

# Print the converted array
print("Original Prices:", prices)
print("Integer Prices:", integer_prices)
print("Data Type:", integer_prices.dtype)
