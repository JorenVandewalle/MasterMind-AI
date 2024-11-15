# MasterMind-AI

## The Team

- Joren Vandewalle 
- Sam De Wispelaere 
- Niels Denoo

## The Task

We are going to create a AI that will guess the correct code of 4 letters which represent colors similair to the mastermind game. We will be using python. 

It will first be made as console game and later to be a visual game where u can select the colors.

## Mastermind Game Rules

### Objective
The objective of **Mastermind** is for the **codebreaker** to guess the secret code chosen by the **codemaker** in as few guesses as possible.

### Players
- **Codemaker**: The player who creates a secret code.
- **Codebreaker**: The player who attempts to guess the secret code.

### Setup
- The **codemaker** secretly selects a code consisting of a sequence of colors.
- The **codebreaker** must guess the code.
- **Colors**: Typically, there are 6 colors to choose from.
- **Positions**: The code consists of a set number of positions (usually 4 positions in a standard version).

### Gameplay
1. **Codemaker's Role**:
   - The codemaker secretly selects a code.
   - The codemaker provides feedback on the codebreaker's guesses, but does not reveal the code directly.

2. **Codebreaker's Role**:
   - The codebreaker makes guesses about the secret code.
   - After each guess, the codemaker provides feedback to indicate how accurate the guess is.

### Feedback
The codemaker provides feedback in the form of **pegs**:
- **Black Pegs**: A black peg indicates that a color is correct and in the correct position.
- **White Pegs**: A white peg indicates that a color is correct but in the wrong position.

The codebreaker uses this feedback to refine their guesses.

#### Example:
If the secret code is `(1, 2, 3, 4)` and the codebreaker guesses `(1, 3, 2, 4)`, the feedback might be:
- **2 black pegs** (because `1` and `4` are in the correct positions).
- **2 white pegs** (because `2` and `3` are the correct colors but in the wrong positions).

### Winning the Game
The codebreaker wins the game by correctly guessing the secret code. The game ends when the codebreaker guesses the code correctly, or when the codemaker decides to end the game.

### Variations
- **Number of Colors**: The number of colors can vary, but typically there are 6 colors.
- **Number of Positions**: The code can have a varying number of positions (usually 4 or 5).
- **Difficulty**: The difficulty can be adjusted by changing the number of colors or positions.

### Player versus player

We made or own little demo for player versus player if u want to try the game for urself.

[Try the player vs player](./PlayerVsPlayer/peoplePlay.py)

---


## Simple step by step

![Project Picture AI](./resources/images/Simple_Explenation.png)



