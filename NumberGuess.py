import random

def guess_the_number():
    """
    A simple number guessing game.
    The user tries to guess a randomly generated number between 1 and 100.
    The game provides hints and keeps track of the number of attempts.
    """
    
    try:
        secret_number = random.randint(1, 10)
    except Exception as e:
        print(f"Error generating a random number: {e}")
        return

    attempts = 0
    guess = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")
    
    while guess != secret_number:
        try:
            user_input = input("Enter your guess: ")
            guess = int(user_input)
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue  

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guess_the_number()
