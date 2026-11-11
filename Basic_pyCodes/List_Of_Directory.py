#List of Dictionaries: Given the following data:
    #employees = [
     #   {"name": "John", "age": 25, "salary": 30000},
      #  {"name": "Alice", "age": 30, "salary": 50000},
       # {"name": "Bob", "age": 28, "salary": 40000},
        #{"name": "David", "age": 35, "salary": 60000} ]
   # Perform the following:
    #* Find the employee with the highest salary.
    #* Filter employees whose salary is greater than 35,000.
    #* Calculate the average salary.
    #* Create a list containing only employee names.
   employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]
highest_salary = max(employees, key=lambda emp: emp["salary"])
print("Employee with highest salary:", highest_salary)
filtered_employees = [
    emp for emp in employees if emp["salary"] > 35000
]
print("Employees with salary greater than 35000:", filtered_employees)
average_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Average salary:", average_salary)
employee_names = [emp["name"] for emp in employees]
print("Employee names:", employee_names)
