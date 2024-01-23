# Number Guessing Game

A simple number guessing game implemented in Python. The computer generates a random number within a specified range, and the user tries to guess it.

## How to Play

1. The computer will randomly choose a number within a given range.
2. The program will display a range of numbers within which the user should guess.
3. The user enters their guess.
4. If the user's guess is correct, they win. Otherwise, the correct number is revealed.

## Files

- `guess_number.py`: Python module containing the game functions.
  - `guess_number(num1, num2)`: Generates a random number between `num1` and `num2`.
  - `range_of_number(range_var)`: Generates a dictionary with random minimum and maximum values within a specified range.
  - `show_on_screen(c_num, df)`: Displays the range of possible numbers on the screen based on the computer's number and the dictionary.
  - `take_user_input()`: Takes user input for their guess.
  - `check_user_input(c_num, u_num)`: Checks if the user's guess matches the computer's number.

- `main.py`: Main script to play the game.
  - Initializes the game by generating a random number and a range of numbers.
  - Displays the range to the user.
  - Takes user input and checks if it matches the computer's number.

## How to Run

Run the `main.py` script to play the game. Follow the on-screen instructions to make your guesses.


python main.py
