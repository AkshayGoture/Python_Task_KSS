# Create a Number Guessing Game where: 
#The program generates a random number between 1 and 50 using random. 
# The user has 5 attempts to guess the number. 
# After each guess, calculate the absolute difference using math.fabs() and display how far the guess is from the correct number.
import random
import math
number = random.randint(1, 50)
for i in range(5):
    guess = int(input("Guess a number (1-50): "))
    difference = math.fabs(number - guess)
    print("Difference:", difference)
    if guess == number:
        print("Congratulations! Correct guess.")
        break
    else:
        print("Wrong guess! Try again.")
else:
    print("Game over! The number was:", number)
