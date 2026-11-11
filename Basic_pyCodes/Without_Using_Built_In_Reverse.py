#String Reversal: Write a program to reverse a string without using built-in reverse functions.
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
