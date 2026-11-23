#A teacher stores marks of students in two subjects: [[78, 85], [90, 88], [67, 72]] 
#Task: ● Convert it to a NumPy array. ● Access the second student's second subject mark.

import numpy as np
# Marks of students in two subjects
marks = [[78, 85],
         [90, 88],
         [67, 72]]

# Convert the list into a NumPy array
arr = np.array(marks)

# Access the second student's second subject mark
print("Second Student's Second Subject Mark:", arr[1, 1])
