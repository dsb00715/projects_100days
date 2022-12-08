""" 
Step 5
from english_words import english_words_lower_alpha_set
word_list = list(english_words_lower_alpha_set)

TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
Delete this line: word_list = ["ardvark", "baboon", "camel"]

TODO-2: - Import the stages from hangman_art.py and make this error go away.
TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word. 
"""

import random
from hangman_words import word_list
from hangman_art import logo, stages


chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)
# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # To check if user has already guessed a letter
    if guess in display:
        print(f"You've already guessed {guess} before. Try again!")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        """ print(
            f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}"
        ) """
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! {guess} not in the word. you've lost one life")
        if lives == 0:
            end_of_game = True
            print("You lost all lives! Play again.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
