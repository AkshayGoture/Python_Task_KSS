#Write a program to perform left shift (<<) and right shift (>>) operations on a number.
num = int(input("Enter a number: "))
positions = int(input("Enter the number of positions to shift: "))
left_shift = num << positions
right_shift = num >> positions
print("Left Shift result:", left_shift)
print("Right Shift result:", right_shift)
