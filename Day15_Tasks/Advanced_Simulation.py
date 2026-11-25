#Advanced Simulation System 
#Scenario: Simulate exam results and generate reports. 
#Task: ● Generate random marks using random ● Store in NumPy array ● Convert to Pandas DataFrame ● Use OOP to represent Student 
#● Use conditions + loops to assign grades ● Save report to file ● Handle errors using try-except ● Use math module for statistics

import random
import numpy as np
import pandas as pd
import math

# OOP: Create Student class
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.grade = ""

    # Assign grade using conditions
    def assign_grade(self):
        if self.marks >= 90:
            self.grade = "A"
        elif self.marks >= 75:
            self.grade = "B"
        elif self.marks >= 60:
            self.grade = "C"
        elif self.marks >= 40:
            self.grade = "D"
        else:
            self.grade = "Fail"

# Main program
try:

    # Student names
    names = ["A", "B", "C", "D", "E"]

    # Generate random marks
    marks = [random.randint(0, 100) for i in range(5)]

    # Store marks in NumPy array
    arr = np.array(marks)

    # Convert into Pandas DataFrame
    df = pd.DataFrame({
        "Name": names,
        "Marks": arr
    })

    # Create Student objects
    students = []

    for i in range(len(names)):
        s = Student(names[i], marks[i])
        s.assign_grade()
        students.append(s)

    # Add grades to DataFrame
    grades = []

    for s in students:
        grades.append(s.grade)

    df["Grade"] = grades

    # Calculate statistics using math module
    average = math.fsum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Calculate standard deviation
    std_dev = math.sqrt(
        sum((x - average) ** 2 for x in marks) / len(marks)
    )

    # Display report
    print("EXAM RESULT REPORT")
    print("------------------")
    print(df)

    print("\nSTATISTICS")
    print("Average Marks:", round(average, 2))
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)
    print("Standard Deviation:", round(std_dev, 2))

    # Save report to CSV file
    df.to_csv("exam_report.csv", index=False)

    print("\nReport saved successfully!")

except ZeroDivisionError:
    print("Error: Cannot calculate average.")

except ValueError:
    print("Error: Invalid data value.")

except PermissionError:
    print("Error: Permission denied while saving file.")

except Exception as e:
    print("Unexpected Error:", e)
