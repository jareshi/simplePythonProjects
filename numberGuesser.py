# This is a simple number guessing game where the user has to guess a randomly selected number within a specified range.

import random

print("Welcome to the Number Guessing Game!")
STARTATTEMPTS = 0  # Number of attempts to start the game

while True:
    rangeMax = input("Enter a positive number: ")
    STARTATTEMPTS += 1

    if rangeMax.isdigit():
        rangeMax = int(rangeMax)
        if rangeMax <= 0:
            print("Please enter a positive integer.")
            if STARTATTEMPTS == 4:
                print("Too many invalid attempts. Exiting the game.")
                quit()
            continue
        break
    else:
        print("Invalid input. Please enter a positive integer.")
        if STARTATTEMPTS == 4:
            print("Too many invalid attempts. Exiting the game.")
            quit()
        continue

secretNumber = random.randint(1, rangeMax)
GUESS = 0
print(f"Alrighty then! I've selected a secret number between 1 and {rangeMax}. Try to guess it!")

while True:
    GUESS += 1
    userGuess = input("Enter your guess: ")

    if userGuess.isdigit():
        userGuess = int(userGuess)
        if userGuess < 1 or userGuess > rangeMax:
            print(f"Your guess must be between 1 and {rangeMax}. Try again.")
            continue
    else:
        print("Invalid input. Please enter a valid number.")
        continue

    if userGuess < secretNumber:
        print("Too low! Try again.")
    elif userGuess > secretNumber:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the secret number {secretNumber}!")
        break

print(f"It took you {GUESS} attempts to guess the number.")
print("Thanks for playing the Number Guessing Game!")

# JHAP