#Student Score Processor 
#Scenario: A teacher stores student names and marks in a list of tuples. 
#Task: ● Convert data into a dictionary ● Use a loop + condition to find students scoring above 50 ● Use math module to calculate average ● Store results in a text file

import math

# List of tuples
students = [
    ("A", 80),
    ("B", 40),
    ("C", 70),
    ("D", 90),
    ("E", 30)
]

# Convert into dictionary
data = dict(students)

# Find students scoring above 50
passed = {}

for name, marks in data.items():
    if marks > 50:
        passed[name] = marks

# Calculate average using math module
average = math.fsum(data.values()) / len(data)

# Display results
print("Student Scores:", data)
print("\nStudents scoring above 50:")

for name, marks in passed.items():
    print(name, marks)

print("\nAverage Marks:", average)

# Save results to text file
with open("student_report.txt", "w") as file:
    file.write("Student Report\n")
    file.write(str(data) + "\n")
    file.write("Passed Students:\n")

    for name, marks in passed.items():
        file.write(f"{name}: {marks}\n")

    file.write(f"Average Marks: {average}")

print("\nReport saved successfully!")
