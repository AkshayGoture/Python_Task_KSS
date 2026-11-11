#Dictionary Sorting: Given a dictionary:
    #students = {"Rahul": 85,"Amit": 92,"Priya": 78,"Sneha": 95}
#Sort the dictionary based on marks in descending order and print the top two students.

students = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 78,
    "Sneha": 95
}
sorted_students = dict(sorted(students.items(),
                              key=lambda item: item[1],
                              reverse=True))
print("Students sorted by marks:")
print(sorted_students)
print("\nTop two students:")
for name, marks in list(sorted_students.items())[:2]:
    print(name, ":", marks)
