import random

# This generates a random number between 1-100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Loops until user guesses the correct number.
while True:
    guess = input("Enter your guess: ")

# Checks if input from user is a number
    if not guess.isdigit():
        print("Please ebter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    # Comparing the guess with the secret number
    if guess < secret_number:
        print("Too low! Try another number.")
    elif guess > secret_number:
        print("Too high! Try another number.")
    else:
        print(f"That's correct! You guessed it in {attempts} tries!")
        break