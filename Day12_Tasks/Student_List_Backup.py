#A teacher has a list of student marks: marks = [50, 60, 70, 80] 
#Scenario: She creates a backup using assignment: backup = marks 
#Task: ● Modify the first element in marks. ● Observe the change in backup. ● Explain why both lists are affected. 
# Original list of student marks

marks = [50, 60, 70, 80]
# Create backup using assignment
backup = marks

# Modify the first element
marks[0] = 100

# Display both lists
print("Original marks:", marks)
print("Backup marks:", backup)
