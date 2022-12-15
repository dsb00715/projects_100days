from art import logo
import random
from os import system


def add(user_list, comp_list):
    pass


def calculate_winner(user_list, comp_list):
    print(f"your final hand: {user_list}, final score: {sum(user_list)}")
    print(f"Computer's final hand: {comp_list}, final score: {sum(comp_list)}")
    if sum(user_list) == 21:
        print("Congratulations! You win with a Blackjack!")
    elif sum(comp_list) == 21:
        print("Oh no! Computer wins with a Blackjack!")


print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 10]
main_loop = True
while main_loop:
    cont = True
    user_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    while cont:
        if user_play == "y":
            system("cls")
            print(logo)
            user_list = random.sample(list(set(cards)), 2)
            comp_list = random.sample(list(set(cards)), 2)

            print(f"your cards: {user_list}, current score: {sum(user_list)}")
            print(f"Computer's first card:{comp_list[0]}")

            if sum(user_list) == 21 or sum(comp_list) == 21:
                calculate_winner(user_list, comp_list)
                cont = False
                break

            should_continue = True
            while should_continue:
                play_again = input("Type 'y' to get another card, Type 'n' to pass:")
                if play_again == "n":
                    calculate_winner(user_list, comp_list)
                    should_continue = False
                    break
                elif play_again == "y":
                    add(user_list, comp_list)
                else:
                    print("please input either 'y' or 'n':")
        elif user_play == "n":
            main_loop = False
            break
        else:
            print("Please enter either 'y' or 'n':")