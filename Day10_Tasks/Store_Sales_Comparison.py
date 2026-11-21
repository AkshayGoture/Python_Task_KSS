#Two stores record daily sales for 3 days. 
#Scenario: Store A = [200, 250, 300] Store B = [180, 270, 310] 
#Task: ● Store them in NumPy arrays. ● Find the daily difference in sales between the two stores. ● Print the resulting array.

import numpy as np
# Daily sales of two stores
Store_A = [200, 250, 300]
Store_B = [180, 270, 310]

# Convert lists into NumPy arrays
array_A = np.array(Store_A)
array_B = np.array(Store_B)

# Find the daily difference in sales
difference = array_A - array_B

# Print the resulting array
print("Daily Sales Difference:", difference)
