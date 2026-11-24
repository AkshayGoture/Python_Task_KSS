 #A company stores employee data: employees = [[101, "A"], [102, "B"], [103, "C"]] 
#Scenario: ● Create a shallow copy of the list. ● Modify one nested list (e.g., change "A" to "Z"). ● Observe changes in both lists. 
#Task: ● Explain why the change reflects in both. ● Fix it using deep copy. 

nums = [1, 2, 3, 4, 5, 6]

# Filter even numbers using list comprehension
even_numbers = [n for n in nums if n % 2 == 0]

# Display the result
print("Even numbers:", even_numbers)
