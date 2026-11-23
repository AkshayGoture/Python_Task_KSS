#A system stores customer names: ["Ravi", "Anil", "Sita", "John"] 
#Task: ● Convert it to a NumPy array. ● Sort the names alphabetically.

import numpy as np

# Given customer names
names = ["Ravi", "Anil", "Sita", "John"]

# Convert list into NumPy array
customer_names = np.array(names)

# Sort names alphabetically
sorted_names = np.sort(customer_names)

# Display the result
print("Sorted customer names:", sorted_names)
