
#A data pipeline receives the following array: [12, 7, 25, 3, 18, 10] 
#Scenario: 1. Convert the list into a NumPy array. 2. Sort the array. 3. Split the sorted array into two equal parts. 4. Calculate the sum of each part. 
#Output: ● Sorted array ● Two split arrays ● Sum of each part

import numpy as np
# Given data
data = [12, 7, 25, 3, 18, 10]

# Step 1: Convert the list into a NumPy array
data_array = np.array(data)

# Step 2: Sort the array
sorted_array = np.sort(data_array)

# Step 3: Split the sorted array into two equal parts
split_arrays = np.split(sorted_array, 2)

# Step 4: Calculate the sum of each part
sum1 = np.sum(split_arrays[0])
sum2 = np.sum(split_arrays[1])

# Print the results
print("Sorted Array:", sorted_array)

print("First Split Array:", split_arrays[0])
print("Second Split Array:", split_arrays[1])

print("Sum of First Part:", sum1)
print("Sum of Second Part:", sum2)
