# Write a program to check whether a substring exists in a string.
string = input("Enter a string: ")
substring = input("Enter a substring to search: ")
if substring in string:
    print("Substring exists in the string.")
else:
    print("Substring does not exist in the string.")
