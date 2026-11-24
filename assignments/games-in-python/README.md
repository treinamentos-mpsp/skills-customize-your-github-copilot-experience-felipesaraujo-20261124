
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game that uses strings, loops, conditionals, and user input to help players guess a hidden word before their attempts run out.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description

Complete `starter-code.py` to create a word-guessing game. The program should select a secret word, accept letter guesses from the player, and display the player's progress after each attempt.

#### Requirements

The completed program must:

- Randomly select a word from the `words` list
- Initialize the guessed letters and remaining incorrect guesses
- Accept one letter guess at a time
- Display the hidden word as letters and underscores, such as `_ y t h o _`
- Add the guessed letter to the state when it is correct
- Reduce the remaining attempts when the guess is incorrect
- End the game when the word is fully revealed or attempts run out
- Display a victory or defeat message at the end