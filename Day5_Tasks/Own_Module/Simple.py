import Calculator
print("===== SIMPLE CALCULATOR =====")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("Enter your choice (1-4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
    result = calculator.addition(num1, num2)
    print("Result:", result)
elif choice == '2':
    result = calculator.subtraction(num1, num2)
    print("Result:", result)
elif choice == '3':
    result = calculator.multiplication(num1, num2)
    print("Result:", result)
elif choice == '4':
    result = calculator.division(num1, num2)
    print("Result:", result)
else:
    print("Invalid choice! Please select between 1 and 4.")
