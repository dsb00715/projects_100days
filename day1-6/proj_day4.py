import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇
list_op = [rock, paper, scissors]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")
)
if user_choice >= 3 or user_choice < 0:
    print("invalid Choice, you lose!!!")
    exit(0)
else:
    print(list_op[user_choice])

comp_choice = random.randint(0, 2)
print(f"Computer choose: \n{list_op[comp_choice]}")

if list_op[user_choice] == list_op[comp_choice]:
    print("It's a draw!!!")
elif user_choice == 0:
    if comp_choice == 1:
        print("you lose!😥")
    else:
        print("Congratulations! You Win🏆")
elif user_choice == 1:
    if comp_choice == 2:
        print("you lose!😥")
    else:
        print("Congratulations! You Win🏆")
elif user_choice == 2:
    if comp_choice == 0:
        print("you lose!😥")
    else:
        print("Congratulations! You Win🏆")
