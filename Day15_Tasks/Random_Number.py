#Random Number Analyzer 
#Scenario: A system generates random numbers for testing. 
#Task: ● Use random to generate 10 numbers ● Store in a list ● Use loop + condition to count even/odd numbers ● Use set to remove duplicates

import random

# Generate 10 random numbers
numbers = []

for i in range(10):
    numbers.append(random.randint(1, 100))

# Count even and odd numbers
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

# Remove duplicates using set
unique = set(numbers)

# Display results
print("Random Numbers:", numbers)
print("Even Count:", even)
print("Odd Count:", odd)
print("Unique Numbers:", unique)
