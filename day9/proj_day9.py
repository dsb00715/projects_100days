from art import logo
from os import system

# print ascii art & define variables
print(logo)
dict_bidders = {}
re_run = True

# Please refet to flowchart for more info about the logic(https://drive.google.com/file/d/1Sw4E4-i9g_MF1u9i-_Il5l0NOudmHJMu/view?usp=sharing)
while re_run:
    name = input("What is your name?: ").lower()
    bid = int(input("What is your bid?: $"))
    dict_bidders[name] = bid
    other = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other == "yes":
        system("cls")
    else:
        # another way to get max values & keys are geeting them by running a loop on Dictionary keys
        winner = max(dict_bidders, key=dict_bidders.get)
        max_bid = max(dict_bidders.values())
        print(f"The winner is {winner} with a bid of ${max_bid}.")
        re_run = False
