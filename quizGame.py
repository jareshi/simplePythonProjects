"""This is a simple quiz game in Python that tests the user's knowledge about computers."""

print("Welcome to the Python Quiz Game!")
STARTATTEMPTS = 0 # Number of attempts to start the game

while STARTATTEMPTS < 4:
    CORRECT = 0 # Number of CORRECT answers
    INCORRECT = 0 # Number of INCORRECT answers
    startGame = input("Would you like to play? ([Y]es/[N]o): ").lower()

    if startGame == "y" or startGame == "yes":
        print("Bet, let's get started!")
        print("You will be asked 6 questions about computers. Try to answer them CORRECTly!")
        break

    # If the user enters 'n' or 'no', the game will exit
    elif startGame == "n" or startGame == "no":
        print("Okay, maybe next time!")
        quit()

    # If the user enters something other than 'y', 'yes', 'n', or 'no', they will be prompted again
    else:
        print("Invalid input. Please enter '[Y]es' or '[N]o'.")
        STARTATTEMPTS += 1

if STARTATTEMPTS == 4:
    print("Too many invalid attempts. Exiting the game.")
    quit()

# Question 1
answer1 = input("\n1. What does CPU stand for? (a) Central Processing Unit (b) Computer Personal Unit: ").lower()
if answer1 == "a":
    print("CORRECT!")
    CORRECT += 1
else:
    print("INCORRECT. The CORRECT answer is (a) Central Processing Unit.")
    INCORRECT += 1

# Question 2
answer2 = input("\n2. What does RAM stand for? (a) Read Access Memory (b) Random Access Memory: ").lower()
if answer2 == "b":
    print("CORRECT!")
    CORRECT += 1
else:
    print("INCORRECT. The CORRECT answer is (b) Random Access Memory.")
    INCORRECT += 1

# Question 3
answer3 = input("\n3. What does GPU stand for? (a) Graphics Processing Unit (b) General Processing Unit: ").lower()
if answer3 == "a":
    print("CORRECT!")
    CORRECT += 1
else:
    print("INCORRECT. The CORRECT answer is (a) Graphics Processing Unit.")
    INCORRECT += 1

# Question 4
answer4 = input("\n4. What does SSD stand for? (a) Super Speed Drive (b) Solid State Drive: ").lower()
if answer4 == "b":
    print("CORRECT!")
    CORRECT += 1
else:
    print("INCORRECT. The CORRECT answer is (b) Solid State Drive.")
    INCORRECT += 1

# Question 5
answer5 = input("\n5. What does HDD stand for? (a) Hard Disk Drive (b) High Density Drive: ").lower()
if answer5 == "a":
    print("CORRECT!")
    CORRECT += 1
else:
    print("INCORRECT. The CORRECT answer is (a) Hard Disk Drive.")
    INCORRECT += 1

# Question 6
answer6 = input("\n6. What does BIOS stand for? (a) Basic Input Output System (b) Binary Input Output System: ").lower()
if answer6 == "a":
    print("CORRECT!")
    CORRECT += 1
else:
    print("INCORRECT. The CORRECT answer is (a) Basic Input Output System.")
    INCORRECT += 1

# Final score
print(f"\nYou answered {CORRECT} questions CORRECTly and {INCORRECT} questions INCORRECTly.")
if CORRECT >= 5:
    print("Congratulations! You are a computer whiz!")
    quit()
elif CORRECT >= 3:
    print("Good job! You have a decent understanding of computers.")
    quit()
else:
    print("Keep learning! You can improve your knowledge of computers.")
    quit()

# JHAP