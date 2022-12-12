from art import logo
import random
from os import system


def add(user_list, comp_list):
    pass


def calculate_winner(user_list, comp_list):
    pass


# print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cont = True
while cont:
    user_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if user_play == "y":
        system("cls")
        print(logo)
        user_list = random.sample(list(set(cards)), 2)
        sum_user_list = sum(user_list)
        comp_list = random.sample(list(set(cards)), 2)
        sum_comp_list = sum(comp_list)
        if sum_user_list == 21:
            print()

        print(f"your cards: {user_list}, current score: {sum_user_list}")
        print(f"Computer's first card:{comp_list[0]}")

        should_continue = True
        while should_continue:
            play_again = input("Type 'y' to get another card, Type 'n' to pass:")
            if play_again == "n":
                calculate_winner(user_list, comp_list)
                should_continue = False
            elif play_again == "y":
                add(user_list, comp_list)
            else:
                print("please input either 'y' or 'n':")
    elif user_play == "n":
        cont = False
    else:
        print("Please enter either 'y' or 'n':")
