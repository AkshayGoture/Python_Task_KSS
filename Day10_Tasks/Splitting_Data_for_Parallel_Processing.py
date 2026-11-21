 Splitting Data for Parallel Processing 
#A dataset contains the following values: [5, 10, 15, 20, 25, 30] 
#Scenario: You want to distribute the data across 3 processors. 
#Task: ● Store the data in a NumPy array. ● Split it into 3 equal parts using NumPy.

import numpy as np
# Given dataset
data = [5, 10, 15, 20, 25, 30]

# Convert the list into a NumPy array
data_array = np.array(data)

# Split the array into 3 equal parts
split_data = np.split(data_array, 3)

# Print the split arrays
print("Original Array:")
print(data_array)

print("Data Split into 3 Parts:")
for part in split_data:
    print(part)
