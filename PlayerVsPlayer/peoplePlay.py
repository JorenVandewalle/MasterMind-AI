import os

def clear_terminal():
    os.system('cls')

def get_feedback(code, guess):
    """Provides feedback: black pegs for correct color in correct position, white pegs for correct color in wrong position."""
    black_pegs = sum([c == g for c, g in zip(code, guess)])  # Correct color & position
    white_pegs = sum([min(code.count(c), guess.count(c)) for c in set(guess)]) - black_pegs  # Correct color, wrong position
    return black_pegs, white_pegs

def mastermind_game():
    # List of possible colors
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Red, Green, Blue, Yellow, Orange, Purple

    print("Welcome to Mastermind!\n")
    print("One player will create a secret color code, and the other player will try to guess it.")
    print("After each guess, feedback will be provided in the form of black and white pegs.")
    print("Black pegs indicate correct color in the correct position.")
    print("White pegs indicate correct color but in the wrong position.\n")

    # Set the length of the code to always be 4
    code_length = 4

    # Player 1 enters a secret code
    print("\nPlayer 1, create your secret code (don't tell Player 2!).")
    code = input(f"Enter your secret {code_length}-color code (using colors: {', '.join(colors)}): ").upper()

    # Validate that the code is the right length and uses valid colors
    while (len(code) != code_length or any(c not in colors for c in code)):
        print(f"Invalid code! Please use {code_length} colors from: {colors}.")
        code = input(f"Enter your secret {code_length}-color code (using colors: {', '.join(colors)}): ").upper()

    clear_terminal()

    # Player 2 starts guessing the code
    attempts = 0
    print("\nPlayer 2, start guessing!\n")

    while True:
        # Player 2 enters their guess
        guess = input(f"Attempt {attempts + 1}: Enter your guess (e.g., RGBY): ").upper()

        # Validate guess length and colors
        while (len(guess) != code_length or any(c not in colors for c in guess)):
            print(f"Invalid guess! Please use {code_length} colors from: {colors}.")
            guess = input(f"Attempt {attempts + 1}: Enter your guess (e.g., RGBY): ").upper()

        # Get feedback for the guess
        black_pegs, white_pegs = get_feedback(code, guess)
        print(f"Feedback: {black_pegs} black peg(s), {white_pegs} white peg(s)\n")

        attempts += 1

        if black_pegs == code_length:
            print(f"Congratulations Player 2! You've cracked the code {code} in {attempts} attempts.")
            break

# Run the game
mastermind_game()

