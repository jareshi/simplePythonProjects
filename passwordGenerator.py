"""This is a simple password generator program that creates random passwords based on user-defined criteria."""

import random
import string

print("Welcome to the Password Generator program!")

def generate_password(length, use_uppercase = True, use_digits = True, use_special_chars = True):
    """Generates a random password based on the specified criteria."""
    lowercase = string.ascii_lowercase  # Always include lowercase letters
    digits = string.digits if use_digits else ''
    uppercase = string.ascii_uppercase if use_uppercase else ''
    special_chars = string.punctuation if use_special_chars else ''

    characterSet = lowercase + digits + uppercase + special_chars

    pwd_chars = []

    # Ensure at least one character from each selected set
    if use_uppercase:
        pwd_chars.append(random.choice(uppercase))
    if use_digits:
        pwd_chars.append(random.choice(digits))
    if use_special_chars:
        pwd_chars.append(random.choice(special_chars))

    # Fill the rest with random choices from the full set
    while len(pwd_chars) < length:
        pwd_chars.append(random.choice(characterSet))

    # Shuffle to avoid predictable positions
    random.shuffle(pwd_chars)

    pwd = ''.join(pwd_chars)

    return pwd

def get_yes_no(prompt):
    """Prompt the user until a valid yes/no response is entered."""
    while True:
        response = input(prompt).strip().lower()
        if response in ('yes', 'y'):
            return True
        elif response in ('no', 'n'):
            return False
        else:
            print("Invalid input. Please enter '[Y]es' or '[N]o'.")

userLength = input("Enter the desired password length (minimum 8 characters): ")
while not userLength.isdigit() or int(userLength) < 8:
    print("Invalid input. Please enter a number greater than or equal to 8.")
    userLength = input("Enter the desired password length (minimum 8 characters): ")

userLength = int(userLength)

UPPER = get_yes_no("Include uppercase letters? ([Y]es/[N]o): ")
DIGIT = get_yes_no("Include digits? ([Y]es/[N]o): ")
SPEC = get_yes_no("Include special characters? ([Y]es/[N]o): ")

print(f"Your generated password is: {generate_password(userLength, UPPER, DIGIT, SPEC)}")
print("Thank you for using the Password Generator program!")

# JHAP