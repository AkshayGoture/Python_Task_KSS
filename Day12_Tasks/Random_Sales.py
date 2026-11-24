#A company wants to simulate 10 days of sales (range 100–500). 
#Task: ● Generate random integers using NumPy. ● Print the array. ● Find the average sales.

import numpy as np

# Generate random sales for 10 days
sales = np.random.randint(100, 501, size=10)

# Print sales array
print("Daily Sales:", sales)

# Calculate average sales
average_sales = np.mean(sales)

print("Average Sales:", average_sales)
