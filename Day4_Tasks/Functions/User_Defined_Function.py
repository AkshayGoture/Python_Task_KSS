# Write a function to find the sum of elements in a list using a user-defined function. 
def list_sum(my_list):
    total = 0
    for num in my_list:
        total += num
    return total
numbers = [10, 20, 30, 40, 50]
result = list_sum(numbers)
print("Sum of list elements:", result)
