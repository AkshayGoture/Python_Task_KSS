 #A dataset contains: data = [[1, 2, 3], [4, 5], [6]] 
#Task: ● Flatten the list using list comprehension. ● Then create a new list containing squares of only even numbers.

data = [[1, 2, 3], [4, 5], [6]]

# Flatten the nested list
flattened = [num for sublist in data for num in sublist]

print("Flattened List:", flattened)
