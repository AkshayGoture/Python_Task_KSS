#Employee Management System (OOP + File + Dict) 
#Scenario: Manage employee data. 
#Task: ● Create a class Employee ● Store employees in a dictionary ● Save data to a file ● Use exception handling for invalid salary input ● Use loop to display all employees

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
