# Write a function to check whether a number is even or odd.
def check(num):
    if num % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
n = int(input("Enter a number: "))
check(n)
