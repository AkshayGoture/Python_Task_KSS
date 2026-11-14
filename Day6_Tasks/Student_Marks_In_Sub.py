subjects = ("Maths", "Physics", "Chemistry")
student_names = set()
student_records = {}
def total(marks):
    if not marks:
        return 0
    return marks[0] + total(marks[1:])
def add_student():
    try:
        name = input("Enter name: ")
        if name in student_names:
            print("Student already exists!")
            return

        marks = [float(input(s + ": ")) for s in subjects]
        student_names.add(name)
        student_records[name] = marks
        print("Student added successfully!")

    except ValueError:
        print("Enter numeric marks only!")
def display():
    for name, marks in student_records.items():
        print(name, marks, "Total:", total(marks),
              "Average:", total(marks) / len(marks))
def average():
    try:
        name = input("Enter name: ")
        if name not in student_records:
            raise NameError("Student not found!")

        marks = student_records[name]
        if not isinstance(marks, list):
            raise TypeError("Invalid marks type!")

        print("Average:", total(marks) / len(marks))

    except (NameError, TypeError, ZeroDivisionError) as e:
        print("Error:", e)
while True:
    print("\n1.Add  2.Display  3.Average  4.Exit")
    try:
        ch = int(input("Enter choice: "))

        if ch == 1:
            add_student()
        elif ch == 2:
            display()
        elif ch == 3:
            average()
        elif ch == 4:
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Enter a valid number!")
