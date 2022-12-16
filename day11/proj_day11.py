from art import logo
import random
from os import system


def ace_calculation(l_list):
    l_list = [1 if i == 11 else i for i in l_list]
    while sum(l_list) < 18:
        l_list.append(random.sample(list(set(cards)), 1)[0])
    return l_list


def calculate_winner(user_list, comp_list):
    print(f"your final hand: {user_list}, final score: {sum(user_list)}")
    print(f"Computer's final hand: {comp_list}, final score: {sum(comp_list)}")
    if sum(user_list) == 21:
        print("Congratulations! You win with a Blackjack!")
    elif sum(comp_list) == 21:
        print("Oh no! Computer wins with a Blackjack!")
    elif sum(user_list) > 21:
        print("You loose! you went over!")
    elif sum(comp_list) > 21:
        print("You win! Computer went over!")
    elif sum(user_list) > sum(comp_list):
        print("Congratulations! You win!")
    elif sum(comp_list) > sum(user_list):
        print("Oh no! You loose. try again!")
    elif sum(user_list) == sum(comp_list):
        print("It's a draw!")


print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

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
                    if sum(comp_list) >= 18:
                        if sum(comp_list) > 21 and (11 in comp_list):
                            comp_list = ace_calculation(comp_list)
                        calculate_winner(user_list, comp_list)
                        should_continue = False
                        cont = False
                    else:
                        while sum(comp_list) < 18:
                            comp_list.append(random.sample(list(set(cards)), 1)[0])
                        if sum(comp_list) > 21 and (11 in comp_list):
                            comp_list = ace_calculation(comp_list)
                        calculate_winner(user_list, comp_list)
                        should_continue = False
                        cont = False

                elif play_again == "y":
                    if sum(comp_list) <= 18:
                        user_list.append(random.sample(list(set(cards)), 1)[0])
                        comp_list.append(random.sample(list(set(cards)), 1)[0])
                        if sum(comp_list) > 21 and (11 in comp_list):
                            comp_list = ace_calculation(comp_list)
                        elif sum(user_list) > 21 and (11 in user_list):
                            user_list = ace_calculation(user_list)
                        print(
                            f"your cards: {user_list}, current score: {sum(user_list)}"
                        )
                        print(f"Computer's first card:{comp_list[0]}")
                        if sum(user_list) >= 21 or sum(comp_list) >= 21:
                            calculate_winner(user_list=user_list, comp_list=comp_list)
                            should_continue = False
                            cont = False
                    else:
                        user_list.append(random.sample(list(set(cards)), 1)[0])
                        if sum(comp_list) > 21 and (11 in comp_list):
                            comp_list = ace_calculation(comp_list)
                        elif sum(user_list) > 21 and (11 in user_list):
                            user_list = ace_calculation(user_list)
                        print(
                            f"your cards: {user_list}, current score: {sum(user_list)}"
                        )
                        print(f"Computer's first card:{comp_list[0]}")
                        if sum(user_list) >= 21 or sum(comp_list) >= 21:
                            calculate_winner(user_list=user_list, comp_list=comp_list)
                            should_continue = False
                            cont = False
                else:
                    print("please input either 'y' or 'n':")
        elif user_play == "n":
            main_loop = False
            break
        else:
            print("Please enter either 'y' or 'n':")
