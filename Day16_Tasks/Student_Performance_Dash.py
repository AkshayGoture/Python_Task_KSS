#Student Performance Dashboard 
#Scenario: 
#A school records marks of students in one subject: marks = np.array([45, 67, 89, 56, 72, 91, 38]) students = ["A", "B", "C", "D", "E", "F", "G"] 
#Task: ● Convert to Pandas DataFrame ● Plot: 
#○ Line graph → trend of marks ○ Bar chart → student vs marks ○ Pie chart → Pass (>50) vs Fail ○ Histogram → distribution of marks ○ Scatter plot → index vs marks

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

# Create DataFrame
df = pd.DataFrame({"Student": students, "Marks": marks})
print(df)

# Line Graph
plt.plot(students, marks, marker='o')
plt.title("Marks Trend")
plt.show()

# Bar Chart
plt.bar(students, marks, color='orange')
plt.title("Student vs Marks")
plt.show()

# Pie Chart
passed = np.sum(marks > 50)
failed = np.sum(marks <= 50)

plt.pie([passed, failed], labels=["Pass", "Fail"],
        autopct='%1.1f%%', colors=['green', 'red'])
plt.title("Pass vs Fail")
plt.show()

# Histogram
plt.hist(marks, bins=5, color='skyblue', edgecolor='black')
plt.title("Marks Distribution")
plt.show()

# Scatter Plot
plt.scatter(range(1, 8), marks, color='red')
plt.title("Index vs Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()
