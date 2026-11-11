#Dictionary Operations: Create a dictionary containing student names and marks.
students = {
    "Akshay": 85,
    "Firoz": 90,
    "Amit": 78
}
students["Akshay"] = 95
students["Firoz"] = 88
print("Student Details:")
for name, marks in students.items():
    print(name, ":", marks)
