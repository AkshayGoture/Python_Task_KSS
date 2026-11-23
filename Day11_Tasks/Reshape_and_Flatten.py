#reshape and flatten imagge data
#Scenario: 
#An image is stored as a 2 × 3 matrix: [[1,2,3], [4,5,6]] 
#Task: 1. Convert it into a NumPy array. 2. Flatten the array into 1-D format. 3. Print the flattened array.
import numpy as np
image = [[1, 2, 3],
         [4, 5, 6]]

# 1. Convert into NumPy array
arr = np.array(image)

# 2. Flatten the array into 1-D format
flattened = arr.flatten()

# 3. Print the flattened array
print("Original Array:")
print(arr)

print("Flattened Array:")
print(flattened)
