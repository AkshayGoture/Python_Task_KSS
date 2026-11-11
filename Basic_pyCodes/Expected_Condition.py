#Frequency Counter: Given a string `"programming"`, create a dictionary that counts how many times each character appears.
#Expec ```python {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}
string = "programming"
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)
