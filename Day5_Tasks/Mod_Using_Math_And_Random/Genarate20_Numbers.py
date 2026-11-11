#Write a Python program that generates 20 random numbers between 1 and 200 using the random module and store them in a list. Then using the math module, compute and display: 
#Maximum value 
#Minimum value 
#Square root of the maximum number 
#Logarithm of the minimum number
import random
import math
numbers = [random.randint(1, 200) for i in range(20)]
print("Numbers:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Square root of maximum:", math.sqrt(max(numbers)))
print("Logarithm of minimum:", math.log(min(numbers)))
