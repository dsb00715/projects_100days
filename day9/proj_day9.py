from art import logo
from os import system

print(logo)
dict_bidders = {}
re_run = True

while re_run:
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    dict_bidders[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other == "yes":
        system("cls")
    else:
        winner = max(dict_bidders, key=dict_bidders.get)
        max_bid = max(dict_bidders.values())
        print(f"The winner is {winner} with a bid of ${max_bid}.")
        re_run = False
