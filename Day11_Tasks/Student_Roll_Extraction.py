#A list contains roll numbers: [101, 102, 103, 104, 105, 106] 
#Scenario: You want only the middle students (index 2 to 4). 
#Task: ● Use NumPy slicing to extract those values.

import numpy as np
# Student roll numbers
roll_numbers = [101, 102, 103, 104, 105, 106]

# Convert the list into a NumPy array
arr = np.array(roll_numbers)

# Extract middle students (index 2 to 4)
middle_students = arr[2:5]

# Print the extracted values
print("Middle Student Roll Numbers:", middle_students)
