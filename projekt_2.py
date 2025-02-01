"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Marek Benda
email: czechmarekbenda@gmail.com
"""

import random

def generate_rand_num() -> str:
    """Generates a unique non-repeating 4-digit number."""
    digits = random.sample("123456789", 1) + random.sample("0123456789", 3)
    return "".join(digits)

def input_validation(user_input: str) -> list[str]:
    """
    Validates the player input based on the prescribed game rules.
    
    Returns:
        A list of error messages whenever the input is not valid and shows all(!) the problems with the input to help with correction. 
        If the input is valid, the return list is empty and game proceeds.
    """
    errors = []
    if not user_input.isdigit():
        errors.append("Invalid input! The input must be numeric.")
    if len(user_input) != 4:
        errors.append("Invalid input! The number ought to be a 4-digit one.")
    if user_input[0] == "0":
        errors.append("Invalid input! The number cannot begin with a 0.")
    if len(set(user_input)) != len(user_input):
        errors.append("Invalid input! The digits must be unique.")
    return errors

def play_game():
    """Function used to run the game of the Bulls and Cows."""
    secret_number = generate_rand_num()
    attempts = 0

    print(
        "Hi there!",
        "-" * 47,
        "I've generated a random 4-digit number for you.",
        "Let's play a Bulls and Cows game.",
        "-" * 47,
        "Enter a number:",
        "-" * 47,
        sep="\n"
    )

    while True:
        guess = input(">>> ")
        errors = input_validation(guess)

        if errors:
            print("\n".join(errors))
            continue

        attempts += 1
        bulls = sum(1 for i in range(4) if guess[i] == secret_number[i])
        cows = sum(1 for i in range(4) if guess[i] in secret_number and guess[i] != secret_number[i])

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} guess{'es' if attempts != 1 else ''}!")
            print("-" * 47)
            print("That's amazing!")
            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")
            print("-" * 47)

if __name__ == "__main__":
    play_game()
