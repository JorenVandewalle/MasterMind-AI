import itertools
from collections import Counter

# Step 1: Generate all possible codes
def generate_all_codes(colors, positions):
    return list(itertools.product(colors, repeat=positions))

# Step 2: Calculate feedback for a guess compared to the secret code
def calculate_feedback(guess, code):
    """
    Calculates the feedback for a guess against a given code.
    Returns a tuple (black_pins, white_pins).
    """
    black_pins = sum(g == c for g, c in zip(guess, code))  # Correct color and position
    white_pins = (
        sum((Counter(code) & Counter(guess)).values()) - black_pins
    )  # Correct color, wrong position
    return black_pins, white_pins

# Step 3: Eliminate codes that don't match the feedback
def filter_possible_codes(possible_codes, guess, feedback):
    """
    Filters the list of possible codes based on the feedback from the guess.
    """
    return [
        code
        for code in possible_codes
        if calculate_feedback(guess, code) == feedback
    ]

# Step 4: Determine the "minimax" guess
def choose_next_guess(possible_codes):
    """
    Uses the minimax strategy to select the next guess.
    Tries every possible guess from the remaining possible codes and chooses the one that minimizes the worst-case number
    of remaining possibilities.
    """
    best_guess = None
    smallest_worst_case = float("inf")

    # Try every guess from the remaining possible codes
    for guess in possible_codes:
        # Simulate feedback for every possible solution
        feedback_counts = Counter(
            calculate_feedback(guess, code) for code in possible_codes
        )
        # Determine the worst-case size of remaining possibilities
        worst_case = max(feedback_counts.values())

        if worst_case < smallest_worst_case:
            smallest_worst_case = worst_case
            best_guess = guess

    return best_guess

# Step 5: Main game loop
def knuth_mastermind(secret_code, colors, positions):
    """
    Implements Knuth's Five-Guess Algorithm to solve the secret code.
    """
    # Generate all possible codes and guesses
    all_codes = generate_all_codes(colors, positions)
    possible_codes = all_codes[:]  # Start with all codes as possible solutions

    # Initial guess
    guess ='R', 'R', 'G', 'G'
    attempts = 0

    print("Knuth's Mastermind Solver")
    print("enter a secret code of 4 digits between (R G B Y O P) or enter q to quit")
    tempCode = input().upper()
    if tempCode == "Q":
        return
    tempCode = ' '.join(tempCode)
    secret_code = tuple(tempCode.split())
    print(f"Secret code: {secret_code}")

    # Set of previously guessed codes to avoid repetition
    guessed_codes = set()

    while True:
        attempts += 1
        print(f"\nAttempt {attempts}: Guessing {guess}")

        # Get feedback
        feedback = calculate_feedback(guess, secret_code)
        print(f"Feedback: {feedback[0]} black pins, {feedback[1]} white pins")

        if feedback == (positions, 0):  # All black pins means the guess is correct
            print(f"Secret code {secret_code} solved in {attempts} attempts!")
            break

        # Eliminate impossible codes based on feedback
        possible_codes = filter_possible_codes(possible_codes, guess, feedback)
        print(f"Remaining possibilities: {len(possible_codes)}")

        # Add the current guess to the set of guessed codes to avoid repetitions
        guessed_codes.add(guess)

        # Choose the next guess from remaining possible codes
        guess = choose_next_guess(possible_codes)

        # Ensure that the new guess isn't a repeat of a previous guess
        while guess in guessed_codes:
            print("Repeating guess detected, choosing a new one...")
            possible_codes.remove(guess)
            guess = choose_next_guess(possible_codes, possible_codes)

# Example usage:
if __name__ == "__main__":
    # Parameters for Mastermind
    COLORS = ["R", "G", "B", "Y", "O", "P"]  # Representing the 6 colors
    POSITIONS = 4  # Number of positions in the code

    # Secret code to solve
    secret_code = ("P", "O", "Y", "R")  # Example secret code

    knuth_mastermind(secret_code, COLORS, POSITIONS)
