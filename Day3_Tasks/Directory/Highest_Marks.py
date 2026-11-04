#Write a program to find the student with the highest marks from a dictionary.
students = {
    "Akshay": 85,
    "Praveen": 95,
    "Omkar": 78,
    "Firoz": 90
}
top_student = max(students, key=students.get)
print("Student with highest marks:", top_student)
print("Highest marks:", students[top_student])
