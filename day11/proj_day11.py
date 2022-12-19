from art import logo
import random
from os import system


def ace_calculation(l_list):
    """function to calculate value for ace in Blackjack

    Args:
        l_list (user_list or comp_list ): list for which user wants to replace value 11 or 1 & then increment if needed

    Returns:
        _type_: returns a list with replaced & increased total value that is more than 18.
    """
    l_list = [1 if i == 11 else i for i in l_list]
    while sum(l_list) < 18:
        l_list.append(random.sample(list(set(cards)), 1)[0])
    return l_list


def calculate_winner(user_list, comp_list):
    """function to calculate final winner based on the defined criterias

    Args:
        user_list (_type_): cards that user contains for particular game
        comp_list (_type_): cards that dealer/Computer contains for particular game
    """
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


# Start of the game
print(logo)  # prints the Ascii art!
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # the actual deck of cards

main_loop = True
while main_loop:
    # This is the outermost loop that decides if user (wants to/ continue to) play Blackjack or not
    cont = True
    user_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    while cont:
        if user_play == "y":
            system("cls")
            print(logo)
            user_list = random.sample(list(set(cards)), 2)  # deck for user
            comp_list = random.sample(list(set(cards)), 2)  # deck for Computer / dealer

            print(f"your cards: {user_list}, current score: {sum(user_list)}")
            print(f"Computer's first card:{comp_list[0]}")

            if sum(user_list) == 21 or sum(comp_list) == 21:
                """This loop checks if user wins directly with the blackjack or not!"""
                calculate_winner(user_list, comp_list)
                cont = False
                break

            should_continue = True
            while should_continue:
                play_again = input("Type 'y' to get another card, Type 'n' to pass:")
                if play_again == "n":
                    """When User wants to quit the current game by saying "pass". Only Computer tries to get more cards"""
                    if sum(comp_list) >= 18:
                        # This means We can't increase more & it's time to identify the winner
                        if sum(comp_list) > 21 and (11 in comp_list):
                            comp_list = ace_calculation(comp_list)
                        calculate_winner(user_list, comp_list)
                        should_continue = False
                        cont = False
                    else:
                        # Computer's deck total is still below 18 &
                        # there's still chance to increase the total in order to go close to 21
                        while sum(comp_list) < 18:
                            comp_list.append(random.sample(list(set(cards)), 1)[0])
                        if sum(comp_list) > 21 and (11 in comp_list):
                            comp_list = ace_calculation(comp_list)
                        calculate_winner(user_list, comp_list)
                        should_continue = False
                        cont = False

                elif play_again == "y":
                    """When player wants to continue drawing another card from the main deck!"""
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
            # This stops the Program!
            main_loop = False
            break
        else:
            # To prevent user from pressing any other key
            print("Please enter either 'y' or 'n':")
