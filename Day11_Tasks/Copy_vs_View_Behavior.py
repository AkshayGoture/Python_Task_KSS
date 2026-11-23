#Copy vs View Behavior in Data Processing 
#Scenario: A dataset: [10, 20, 30, 40] 
#Task: ● Create a copy of the array. ● Modify the original array. ● Show that the copy does not change. ● Repeat using view() and observe the difference. 

import numpy as np
arr = np.array([10, 20, 30, 40])

# 1. Create a copy
arr_copy = arr.copy()

# Modify the original array
arr[0] = 100

print("Original array:", arr)
print("Copied array:", arr_copy)

# 2. Create a view
arr_view = arr.view()

# Modify the original array again
arr[1] = 200

print("\nOriginal array:", arr)
print("View array:", arr_view)
