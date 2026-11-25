#Shopping Cart System 
#Scenario: A user adds items to a shopping cart. 
#Task: ● Store items in a list ● Convert to set to remove duplicates ● Use loop + condition to calculate total cost ● Handle invalid input using try-except


cart = []

prices = {
    "apple": 20,
    "banana": 10,
    "milk": 30,
    "bread": 40
}

try:
    n = int(input("Enter number of items: "))

    # Add items to cart
    for i in range(n):
        item = input("Enter item name: ").lower()
        cart.append(item)

    # Remove duplicates
    cart = set(cart)

    # Calculate total cost
    total = 0

    for item in cart:
        if item in prices:
            total += prices[item]
        else:
            print("Invalid item:", item)

    # Display result
    print("\nShopping Cart:", cart)
    print("Total Cost:", total)

except ValueError:
    print("Invalid input! Enter a valid number.")

except Exception as e:
    print("Error:", e)
