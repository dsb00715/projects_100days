# Create a number guessing game

"""
To do list:
1. Print the logo with welcome message & basic print message after clearing screen!
2. Pick Random number from 1 to 100 in the background
3. ask user to choose difficulty & as per the selection, show number of guesses they get. 10 for Easy & 5 for Hard.
4. compare the number user guesses with the randomly picked number on step2. 
5. if user gets it wrong, decrease number of available guesses & print available guesses.
6. else print that they've guessed the correct number
7. if user doesn't guess & they've run out of guesses, print game over message 
"""


from art import logo
import random
from os import system

EASY_CHOICES = 10
HARD_CHOICES = 5

system("cls")
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
# print(f"The correct number:{number}")
difficulty = input("Choose a difficulty: Type 'easy' or 'hard': ")


def choice(n):
    if n == "easy":
        return EASY_CHOICES
    elif n == "hard":
        return HARD_CHOICES
    else:
        print("Please choose either 'easy' or 'hard': \nPlease play again!")
        exit()


guesses = choice(n=difficulty)
while guesses >= 1:
    print(f"you have {guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high! \nGuess again.")
        guesses -= 1
    elif guess < number:
        print("Too low! \nGuess again.")
        guesses -= 1
    elif guess == number:
        print(f"You got it! The answer was {number}.")
        exit()

print("You've run out of guesses, you loose.")
