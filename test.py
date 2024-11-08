import random
import itertools
import time

def get_feedback(code, guess):
    """Provides feedback: black pegs for correct color in correct position, white pegs for correct color in wrong position."""
    black_pegs = sum([c == g for c, g in zip(code, guess)])  # Correct color & position
    white_pegs = sum([min(code.count(c), guess.count(c)) for c in set(guess)]) - black_pegs  # Correct color, wrong position
    return black_pegs, white_pegs

def ai_guess(remaining_combinations):
    """AI makes a random guess from the remaining possible combinations."""
    return random.choice(remaining_combinations)

def mastermind_ai_solver():
    # List of possible colors, expanded to allow for a larger variety
    colors = ['R', 'G', 'B', 'Y', 'O', 'P', 'W', 'C']  # Red, Green, Blue, Yellow, Orange, Purple, White, Cyan
    
    print("Welcome to Mastermind AI Solver!")
    print("The AI will try to guess your secret color code.")
    print("After each guess, provide feedback in the form of black and white pegs.")
    print("Black pegs indicate correct color in correct position.")
    print("White pegs indicate correct color in wrong position.\r\n")
    # Ask the player to enter the length of the color code
    code_length = int(input(f"Enter the length of your color code."))
    # Ask the player to enter a secret code
    code =  input(f"Enter your secret {code_length}-color code (e.g., RGBYOPWC): ").upper()
    
    # Validate that the code is the right length and uses valid colors
    if len(code) != code_length or any(c not in colors for c in code):
        print(f"Invalid code! Please use {code_length} colors from: {colors}.")
        return

    # Create all possible combinations of colors (8 colors, 8 positions)
    all_combinations = list(itertools.product(colors, repeat=code_length))
    attempts = 0
    
    print("\nAI is now trying to guess your code...\n")

    start_time = time.time()  # Start the timer

    while True:
        attempts += 1
        guess = ai_guess(all_combinations)
        guess_str = ''.join(guess)
        
        black_pegs, white_pegs = get_feedback(code, guess_str)
        print(f"Attempt {attempts}: AI guessed {guess_str} -> Feedback: {black_pegs} black peg(s), {white_pegs} white peg(s)")

        if black_pegs == code_length:
            end_time = time.time()  # End the timer
            duration = end_time - start_time
            print(f"\nAI cracked the code {code} in {attempts} attempts and {duration:.2f} seconds!")
            break

        # Narrow down possible combinations based on feedback
        all_combinations = [comb for comb in all_combinations if get_feedback(guess, comb) == (black_pegs, white_pegs)]

# Run the AI solver
mastermind_ai_solver()
