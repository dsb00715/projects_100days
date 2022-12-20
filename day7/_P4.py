# Step 1

""" import random

word_list = ["aardvark", "baboon", "camel"]

# [x] TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# [x] TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# [x] TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = random.choice(word_list)
guess = input("Guess a letter: ").lower()

for l in chosen_word:
    if guess == l:
        print("Right")
    else:
        print("Wrong") """


# **************************************************************************


""" # Step 2

import random
from english_words import english_words_lower_alpha_set

word_list = list(english_words_lower_alpha_set)
chosen_word = random.choice(word_list)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# [x] TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

guess = input("Guess a letter: ").lower()
display = []
for letter in chosen_word:
    display.append("_")

# [x] TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter

# [x] TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)
 """
# **************************************************************************

""" # Step 3

import random
from english_words import english_words_lower_alpha_set

word_list = list(english_words_lower_alpha_set)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# [x] TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.

# Method 1

while "_" in display:

    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
        if letter == guess:
            display[position] = letter

    print(display)
print("You've won") """

# Method 2

""" game_end = False

while not game_end:

    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        )
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        game_end = True
        print("You win.") """


# **************************************************************************

# Step 4
import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# [x] TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        # [x] TODO-2: - If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        print("you loose!")
        end_of_game = True

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(lives)

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # [x] TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
