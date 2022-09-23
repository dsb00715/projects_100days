"""
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
"""


print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_people = int(input("How many people to split the bill? "))

total_share = round((total_bill * (1 + tip / 100)) / split_people, 2)

print(f"Each person should pay: ${total_share}")
