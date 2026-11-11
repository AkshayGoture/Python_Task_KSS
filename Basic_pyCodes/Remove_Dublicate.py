#Remove Duplicates: Given a list `[1, 2, 3, 2, 4, 1, 5, 3]`, remove duplicate elements while preserving the original order. Do not use `set()`.
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)
