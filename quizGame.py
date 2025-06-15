print("Welcome to the Python Quiz Game!")
startAttempts = 0 # Number of attempts to start the game

while startAttempts < 4:
    correct = 0 # Number of correct answers
    incorrect = 0 # Number of incorrect answers
    startGame = input("Would you like to play? ([Y]es/[N]o): ").lower()

    if startGame == "y" or startGame == "yes":
        print("Bet, let's get started!")
        print("You will be asked 6 questions about computers. Try to answer them correctly!")
        break

    # If the user enters 'n' or 'no', the game will exit
    elif startGame == "n" or startGame == "no":
        print("Okay, maybe next time!")
        quit()

    # If the user enters something other than 'y', 'yes', 'n', or 'no', they will be prompted again
    else:
        print("Invalid input. Please enter '[Y]es' or '[N]o'.")
        startAttempts += 1

if startAttempts == 4:
    print("Too many invalid attempts. Exiting the game.")
    quit()

# Question 1
answer1 = input("\n1. What does CPU stand for? (a) Central Processing Unit (b) Computer Personal Unit: ").lower()
if answer1 == "a":
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The correct answer is (a) Central Processing Unit.")
    incorrect += 1

# Question 2
answer2 = input("\n2. What does RAM stand for? (a) Read Access Memory (b) Random Access Memory: ").lower()
if answer2 == "b":
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The correct answer is (b) Random Access Memory.")
    incorrect += 1

# Question 3
answer3 = input("\n3. What does GPU stand for? (a) Graphics Processing Unit (b) General Processing Unit: ").lower()
if answer3 == "a":
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The correct answer is (a) Graphics Processing Unit.")
    incorrect += 1

# Question 4
answer4 = input("\n4. What does SSD stand for? (a) Super Speed Drive (b) Solid State Drive: ").lower()
if answer4 == "b":
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The correct answer is (b) Solid State Drive.")
    incorrect += 1

# Question 5
answer5 = input("\n5. What does HDD stand for? (a) Hard Disk Drive (b) High Density Drive: ").lower()
if answer5 == "a":
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The correct answer is (a) Hard Disk Drive.")
    incorrect += 1

# Question 6
answer6 = input("\n6. What does BIOS stand for? (a) Basic Input Output System (b) Binary Input Output System: ").lower()
if answer6 == "a":
    print("Correct!")
    correct += 1
else:
    print("Incorrect. The correct answer is (a) Basic Input Output System.")
    incorrect += 1

# Final score
print(f"\nYou answered {correct} questions correctly and {incorrect} questions incorrectly.")
if correct >= 5:
    print("Congratulations! You are a computer whiz!")
    quit()
elif correct >= 3:
    print("Good job! You have a decent understanding of computers.")
    quit()
else:
    print("Keep learning! You can improve your knowledge of computers.")
    quit()

# JHAP