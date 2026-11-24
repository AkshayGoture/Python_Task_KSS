#A shop has prices: prices = [100, 200, 300, 400] 
#Scenario: ● Apply a 10% discount only if price > 200. 
#Task: ● Use list comprehension with condition to create updated price list.
prices = [100, 200, 300, 400]

# Apply 10% discount if price > 200
updated_prices = [price * 0.9 if price > 200 else price for price in prices]

print("Original Prices:", prices)
print("Updated Prices:", updated_prices)
