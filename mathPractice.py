"""This is a simple math practice program that quizzes the user on basic arithmetic operations."""
# I wrote it for my brother to help him practice math skills.

import random
import time

print("Welcome to the Math Practice program!")
MIN, MAX = None, None
QUESTIONS = 10 # Number of questions to ask

def equationGenerator(minimum, maximum):
    """Generates a random arithmetic equation and its answer."""
    operations = ['+', '-', '*', '/']
    num1 = random.randint(minimum, maximum)
    num2 = random.randint(minimum, maximum)
    operation = random.choice(operations)

    if operation == '/':
        # Ensure no division by zero and num1 is divisible by num2
        while num2 == 0 or num1 % num2 != 0:
            num1 = random.randint(minimum, maximum)
            num2 = random.randint(minimum, maximum)

    equation = f"{num1} {operation} {num2}"
    answer = None

    # Calculate the answer based on the operation
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        answer = num1 // num2

    return equation, answer

print("Choose the difficulty level:")
print("1. Easy (1-10)")
print("2. Medium (1-50)")
print("3. Hard (1-100)")

difficulty = input("Enter your choice (1/2/3): ")

while difficulty not in ['1', '2', '3']:
    print("Invalid choice. Please select 1, 2, or 3.")
    difficulty = input("Enter your choice (1/2/3): ")

if difficulty == '1':
    MIN, MAX = 1, 10
elif difficulty == '2':
    MIN, MAX = 1, 50
elif difficulty == '3':
    MIN, MAX = 1, 100

print(f"You have chosen the {['Easy', 'Medium', 'Hard'][int(difficulty) - 1]} level.")

INCORRECT = 0
CORRECT = 0

input("Press any key to start the quiz!")
print("------------------------------")

START = time.time()

for i in range(QUESTIONS):
    eq, ans = equationGenerator(MIN, MAX)
    userAnswer = input(f"Question {i + 1}: What is {eq}?\nYour answer: ")
    if userAnswer.lstrip('+-').isdigit():
        userAnswer = int(userAnswer)
        if userAnswer == ans:
            print("Correct!")
            CORRECT += 1
        else:
            print(f"Incorrect! The correct answer is {ans}.")
            INCORRECT += 1
    else:
        print(f"Invalid input. The correct answer is {ans}.")
        INCORRECT += 1

END = time.time()
TIME_TAKEN = END - START

print("------------------------------")
print(f"You answered {CORRECT} questions correctly and {INCORRECT} incorrectly.")
print(f"Time taken: {TIME_TAKEN:.2f} seconds.")
print("Thank you for practicing! Keep up the good work!")

# JHAP