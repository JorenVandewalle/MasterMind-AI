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
def solve_code(secret_code, colors, positions):
    """
    Solves a single secret code using Knuth's Five-Guess Algorithm.
    Returns the number of attempts needed to solve the code.
    """
    # Generate all possible codes and guesses
    all_codes = generate_all_codes(colors, positions)
    possible_codes = all_codes[:]  # Start with all codes as possible solutions

    # Initial guess
    guess = ('R', 'R', 'G', 'G')
    attempts = 0

    # Set of previously guessed codes to avoid repetition
    guessed_codes = set()

    while True:
        attempts += 1

        # Get feedback
        feedback = calculate_feedback(guess, secret_code)

        if feedback == (positions, 0):  # All black pins means the guess is correct
            return attempts

        # Eliminate impossible codes based on feedback
        possible_codes = filter_possible_codes(possible_codes, guess, feedback)

        # Add the current guess to the set of guessed codes to avoid repetitions
        guessed_codes.add(guess)

        # Choose the next guess from remaining possible codes
        guess = choose_next_guess(possible_codes)

        # Ensure that the new guess isn't a repeat of a previous guess
        while guess in guessed_codes:
            possible_codes.remove(guess)
            guess = choose_next_guess(possible_codes)

# Step 6: Test all possible codes
def test_all_codes(colors, positions):
    """
    Tests Knuth's algorithm on all possible secret codes.
    Prints the results and identifies codes that took more than 5 attempts to solve.
    """
    all_codes = generate_all_codes(colors, positions)
    results = {}

    for secret_code in all_codes:
        attempts = solve_code(secret_code, colors, positions)
        results[secret_code] = attempts
        print(f"Tested code: {secret_code}, Attempts: {attempts}")

    # Identify codes that took more than 5 attempts
    hard_codes = [code for code, attempts in results.items() if attempts > 5]

    print(f"\nTotal codes tested: {len(all_codes)}")
    print(f"Codes that took more than 5 attempts: {len(hard_codes)}")
    for code in hard_codes:
        print(f"Code {code} took {results[code]} attempts")

# Example usage
if __name__ == "__main__":
    COLORS = ["R", "G", "B", "Y", "O", "P"]  # Representing the 6 colors
    POSITIONS = 4  # Number of positions in the code

    test_all_codes(COLORS, POSITIONS)

