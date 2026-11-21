  
#A company collects employee counts from two branches. 
#Branch A: [[10, 20], [30, 40]] 
#Branch B: [[5, 15], [25, 35]] 
#Scenario: ● Combine the two matrices. ● Calculate the total employees across all departments. ● Print the combined matrix and total.

import numpy as np
# Employee data from Branch A
branch_A = np.array([
    [10, 20],
    [30, 40]
])

# Employee data from Branch B
branch_B = np.array([
    [5, 15],
    [25, 35]
])

# Combine the two matrices
combined_matrix = np.concatenate((branch_A, branch_B))

# Calculate the total number of employees
total_employees = np.sum(combined_matrix)

# Print the combined matrix and total
print("Combined Employee Matrix:")
print(combined_matrix)

print("Total Employees:", total_employees)
