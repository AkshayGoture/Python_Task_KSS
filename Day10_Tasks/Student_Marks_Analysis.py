# Student Marks Analysis

import numpy as np
# Given marks of 5 students
marks = [45, 67, 89, 56, 72]
# Convert the list into a NumPy array
marks_array = np.array(marks)
# Add 5 grace marks to every student
updated_marks = marks_array + 5
# Print the updated marks
print("Updated Marks:", updated_marks)
