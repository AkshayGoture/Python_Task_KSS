#Basic File Logger 
#Scenario: A system logs user actions. 
#Task: ● Take user input ● Store logs in a file ● Use loop to allow multiple entries ● Handle file errors using exception handling 

# Create Employee class
class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

# Dictionary to store employees
employees = {}

try:
    # Add employee details
    for i in range(3):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        employees[emp_id] = Employee(emp_id, name, salary)

    # Save data to file
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            file.write(
                f"{emp.emp_id}, {emp.name}, {emp.salary}\n"
            )

    # Display employees
    print("\nEmployee Details:")

    for emp in employees.values():
        print(emp.emp_id, emp.name, emp.salary)

    print("\nData saved successfully!")

except ValueError as e:
    print("Invalid salary input:", e)

except Exception as e:
    print("Error:", e)
