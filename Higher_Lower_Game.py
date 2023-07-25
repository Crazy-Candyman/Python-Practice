import random  # imports random module to enable random

"""
This program is a guessing game that requires the user
to input a high-bound # and a low-bound #, the program 
will generate a random # and the user will have to
guess the random number between the high-bound and
low-bound numbers.
"""

highbound = int(input("Enter a highbound number: "))

lowbound = int(input("Enter a lowbound number: "))

random_number = random.randint(lowbound, highbound)  # random integer chosen here

# first guess
guess = int(input(f"Guess a number between {lowbound} and {highbound}: "))

while guess != random_number:  # loop until guess equals random number
    if guess < random_number:
        print("Nope too low")
        guess = int(input(f"Guess again between {lowbound} and {highbound}: "))
        continue
    elif guess > random_number:
        print("Nope too high")
        guess = int(input(f"Guess again between {lowbound} and {highbound}: "))
        continue
    else:
        break

print("YOU WON!")
