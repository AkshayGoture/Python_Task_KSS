products = {"Pen": 10, "Book": 50, "Bag": 500}
categories = {"Stationery", "Accessories"}
details = (("Pen", 10), ("Book", 50), ("Bag", 500))
cart = []
def display():
    print(products)
def add_cart():
    try:
        name = input("Enter product: ")
        if name not in products:
            raise NameError("Product not found!")
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            raise ValueError("Invalid quantity!")
        cart.append((products[name], qty))
    except (ValueError, NameError) as e:
        print(e)
def total(items):
    if not items:
        return 0
    return items[0][0] * items[0][1] + total(items[1:])
def bill():
    try:
        for item in cart:
            if not isinstance(item, tuple):
                raise TypeError("Invalid cart data!")
        print("Total Bill: Rs.", total(cart))
    except (TypeError, ZeroDivisionError) as e:
        print(e)
while True:
    print("\n1.Display  2.Add  3.Bill  4.Exit")
    try:
        ch = int(input("Choice: "))
        if ch == 1:
            display()
        elif ch == 2:
            add_cart()
        elif ch == 3:
            bill()
        elif ch == 4:
            break
        else:
            print("Invalid choice!")
    except ValueError:
        print("Enter a valid number!")
