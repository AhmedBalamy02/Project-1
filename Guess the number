import random

def guess_the_number():
    # Set the range for the random number
    min_number = 1
    max_number = 100

    # Set the number of attempts the player has
    max_attempts = 10

    # Generate a random number
    target_number = random.randint(min_number, max_number)

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {min_number} and {max_number}.")
    print("Can you guess it?")

    attempts = 0
    while attempts < max_attempts:
        attempts += 1
        print(f"\nAttempt {attempts}/{max_attempts}")

        # Get the player's guess
        guess = input("Enter your guess: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess < min_number or guess > max_number:
            print(f"Your guess should be between {min_number} and {max_number}.")
            continue

        # Compare the guess with the target number
        if guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} correctly!")
            return
        elif guess < target_number:
            print("Too low!")
        else:
            print("Too high!")

    print("Sorry, you ran out of attempts!")
    print(f"The number I was thinking of was: {target_number}")

# Start the game
guess_the_number()
