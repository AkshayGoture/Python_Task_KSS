#An e-commerce company stores product prices in a NumPy array. 
#Scenario: Prices = [499, 299, 799, 199, 599] 
#Task: ● Convert it into a NumPy array. ● Sort the prices in ascending order.

import numpy as np
# Given product prices
prices = [499, 299, 799, 199, 599]

# Convert the list into a NumPy array
price_array = np.array(prices)

# Sort the prices in ascending order
sorted_prices = np.sort(price_array)

# Print the sorted prices
print("Sorted Product Prices:", sorted_prices)
