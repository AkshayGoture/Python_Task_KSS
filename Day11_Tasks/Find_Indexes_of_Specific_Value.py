import numpy as np

# Product defect codes
defects = np.array([2, 4, 1, 4, 3, 4, 5])

# Find indexes where value is 4
indexes = np.where(defects == 4)

# Print the indexes
print("Indexes where value = 4:", indexes[0])
