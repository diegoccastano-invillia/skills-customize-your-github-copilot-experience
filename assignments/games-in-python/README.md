# 📘 Assignment: Hangman Game

## 🎯 Objective

Create a classic word-guessing game in Python using strings, loops, conditionals, and user input while practicing core programming logic.

## 📝 Tasks

### 🛠️ Create the Game Setup

#### Descrição
Build the initial structure of the hangman game by choosing a random word from a predefined list and displaying the hidden word as underscores.

#### Requisitos
O programa concluído deve:

- Store a list of words and select one at random.
- Show the secret word as underscores, such as _ _ _ _ _.
- Accept a letter guess from the user.
- Track the letters already guessed and avoid repeated guesses.
- Display the current progress after each attempt.

### 🛠️ Handle Guessing and Attempts

#### Descrição
Implement the gameplay loop so the player continues guessing letters until the word is fully revealed or the maximum number of wrong attempts is reached.

#### Requisitos
O programa concluído deve:

- Count the number of remaining incorrect attempts.
- Reveal correctly guessed letters in their positions.
- Notify the user when a guessed letter is not in the word.
- End the game when the word is solved or the player runs out of attempts.
- Print a clear win or loss message at the end.

### 🛠️ Improve the User Experience

#### Descrição
Add polish to the game by making the output easier to follow and the game flow more user-friendly.

#### Requisitos
O programa concluído deve:

- Show the guessed letters and remaining attempts clearly.
- Use simple, readable messages for each game state.
- Support repeated rounds if desired.
- Keep the game logic easy to understand and maintain.