# Knuth's Algorithm for Mastermind

## Overview

Knuth's algorithm is a well-known method for solving the game of **Mastermind**. The goal of Mastermind is to guess a secret code consisting of a sequence of pegs of different colors. The algorithm minimizes the number of guesses required to determine the secret code by systematically eliminating inconsistent guesses based on feedback received after each guess.

## Objective

- Minimize the number of guesses required to determine the secret code.
- Use feedback after each guess to eliminate possibilities that do not match the clues provided by the game.
- Ensure that every guess follows the constraints of the game.

---

## Mastermind Recap

- In **Mastermind**, the secret code consists of a sequence of 4 pegs (colors).
- Each peg can be any of the available colors (let's say 6 colors: Red, Blue, Green, Yellow, White, and Black).
- After each guess, you get feedback in terms of **black pegs** and **white pegs**:
  - **Black peg**: Correct color in the correct position.
  - **White peg**: Correct color but in the wrong position.

## Knuth's Algorithm Steps

### Step 1: Initial Setup

1. **Generate the Initial Set of All Possible Codes**:
   - In a game with 6 colors and a code length of 4, there are a total of \(6^4 = 1296\) possible codes.
   - At the start of the game, consider all 1296 codes as potential candidates for the secret code.

---

### Step 2: Make an Initial Guess

- Make the first guess as **`1122`** (a commonly chosen initial guess).
- Submit this guess to the game and receive feedback in terms of black and white pegs.

---

### Step 3: Eliminate Inconsistent Codes

For each subsequent guess:

1. **Compare Each Code in the Candidate Set to the Guess**:
    - For each code in the list of possible codes:
        - Simulate the feedback you would get if that code were the secret code and you compared it with your current guess.
        - Determine the number of black and white pegs for each comparison.

2. **Compare Feedback with Actual Game Feedback**:
    - Eliminate any code from the candidate set that would not produce the same feedback (i.e., the same number of black and white pegs) as the feedback received from your guess.

---

### Step 4: Make the Next Guess

- From the remaining candidate codes, select a guess.
  - You can select the first candidate in the remaining list or use some strategy to maximize the chances of eliminating more incorrect codes. (we will use a min-max strategy for this explained later)

- Submit this guess to the game and receive feedback.

- Continue eliminating inconsistent codes based on the feedback.

---

### Step 5: Continue Until the Secret Code is Found

- Keep repeating Steps 3 and 4 until you receive **4 black pegs**, indicating that your guess matches the secret code exactly.
- At this point, you have successfully identified the secret code.

---

## Efficiency of Knuth's Algorithm

- Knuth's algorithm guarantees that the secret code can be identified in **no more than 5 guesses**, no matter the complexity of the code or the feedback.
- This makes Knuth's algorithm a highly efficient and reliable method for solving Mastermind.

---

## Advantages of Knuth's Algorithm

- **Optimal Strategy**: It minimizes the number of guesses required.
- **Systematic Elimination**: Uses the feedback intelligently to reduce the search space of candidate codes quickly.
- **Robustness**: Provides a strong guarantee of solving the game within 5 guesses.

---

## Disadvantages

- **Computational Cost**: Requires comparing each guess against a large set of potential candidate codes (1296 possibilities initially).
- For larger versions of the game (e.g., more colors or longer code lengths), the search space increases exponentially.

---

## Conclusion

Knuth's algorithm for Mastermind is a robust and efficient strategy for minimizing guesses to find the secret code. By systematically eliminating inconsistent guesses based on feedback after each round, the algorithm ensures that a solution is found in no more than 5 guesses.

This method showcases how intelligent searching and elimination based on feedback can drastically reduce the search space in combinatorial games like Mastermind.

---

## Example of Knuth's Algorithm

Let's go step by step with an example to illustrate Knuth's algorithm.

### Setup

- Suppose you are playing a game of Mastermind with a secret code of 4 pegs.
- The available colors are **Red (R), Blue (B), Green (G), Yellow (Y), White (W), and Black (K)**.
- Let's say the secret code is **`RGBY`**.

### Guess 1

- **Initial Guess**: `RRBB` (a common starting guess in Knuth's algorithm).
- Submit this guess to the game and get feedback: say, **1 black peg and 1 white peg**.

### Eliminate Inconsistent Codes

- Compare every code in the candidate list (1296 possibilities) with your guess `RRBB`.
- Remove all codes that do not result in the same feedback (1 black peg and 1 white peg).

### Guess 2

- Make your next guess from the remaining candidate list, such as `RBGW`.
- Submit this guess to the game and receive new feedback: **2 black pegs**.
- Continue eliminating codes that do not match this feedback.

### Continue Until the Secret Code is Found

- After a few iterations, you'll eventually guess **`RGBY`** and receive **4 black pegs**, meaning you've correctly identified the secret code.

By following this systematic elimination process based on Knuth's algorithm, you have minimized the guesses required to determine the secret code efficiently and accurately.


