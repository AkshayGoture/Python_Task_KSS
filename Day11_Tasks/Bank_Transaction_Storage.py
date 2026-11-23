 #A bank stores the transaction amounts of a customer in a list: [1200, 500, 800, 1500] 
#Scenario: ● Convert the list into a NumPy array. ● Print the type of the object. ● Verify that it is a NumPy ndarray.

import numpy as np
# Original list of transaction amounts
transactions = [1200, 500, 800, 1500]

# Convert the list into a NumPy array
arr = np.array(transactions)

# Print the array
print("NumPy Array:", arr)

# Print the type of the object
print("Type of object:", type(arr))

# Verify whether it is a NumPy ndarray
print("Is it a NumPy ndarray?", isinstance(arr, np.ndarray))
