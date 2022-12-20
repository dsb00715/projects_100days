# Import required basic modules & datasets
from game_data import data
from art import *
from random import choice
from os import system


def compare_dataset(followers_a, followers_b, user_selection):
    """Function to calculate result of the comparison between datasets

    Args:
        followers_a (int): followers of first category
        followers_b (int): followers of second category
        user_selection (string): user input

    Returns:
        _type_: True if user is right & False when user is wrong
    """
    if followers_a > followers_b:
        actual_ans = "a"
    else:
        actual_ans = "b"
    if user_selection == actual_ans:
        return True
    else:
        return False


# Create main function
def main():
    print(logo)
    total_score = 0
    should_continue = True

    # choose first random entry from dataset & keep it outside while loop
    cat_a = choice(data)

    while should_continue:
        """While loops that only fails when user is wrong."""
        # choose Second random entry
        cat_b = choice(data)
        if cat_a["name"] == cat_b["name"]:
            """this makes sure that second list is not same as the first one"""
            cat_b = choice(data)

        # print both selected dictionaries along with art and ask for user input!
        print(
            f"Compare A: {cat_a['name']}, a {cat_a['description']}, from {cat_a['country']}"
        )
        print(vs)
        print(
            f"Against B: {cat_b['name']}, a {cat_b['description']}, from {cat_b['country']}"
        )
        user_ans = input("Who has more followers? Type 'A' or 'B':").lower()

        # Call function to get the final result
        result = compare_dataset(
            followers_a=cat_a["follower_count"],
            followers_b=cat_b["follower_count"],
            user_selection=user_ans,
        )

        if result:
            system("cls")
            print(logo)
            total_score += 1
            print(f"You're right! Current score: {total_score}.")
            # Option B becomes Option A now!
            cat_a = cat_b
        else:
            print(f"Sorry, that's wrong. Final score: {total_score}.")
            should_continue = False
            return


# it makes main the basic function
if __name__ == "__main__":
    main()
