##################### Extra Hard Starting Project ######################

# [x]TODO-1: Update the birthdays.csv

# [x]TODO-2: Check if today matches a birthday in the birthdays.csv

# [x]TODO-3: If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# [x]TODO-4: Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import random
import smtplib

# ---------------------------- CONSTANTS ------------------------------- #
BIRTH_FILE = r"day32_SMTPlib_email\birthday_wisher\birthdays.csv"
DATA = r"day32_SMTPlib_email\birthday_wisher\quotes\quotes.txt"
EMAIL = "testgetesten@gmail.com"
PASSWORD = "wmdoeffzjfuabjcg"

# ---------------------------- GET FRIEND'S DATA IN LIST ------------------------------- #
birthday_df = pd.read_csv(BIRTH_FILE)
birthday_list = birthday_df.to_dict(orient="records")

# ---------------------------- CHOOSE RANDOM QUOTE ------------------------------- #
quotes = []
with open(DATA, "r") as f:
    for line in f.readlines():
        quotes.append(line)
quote = random.choice(quotes)

# ---------------------------- CREATE A FUNCTION TO SEND EMAIL ------------------------------- #
def send_email(person_data, quote):
    name = person_data["name"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        message = f"Dear {name},\n\nWish you a many many happy returns of the day.\n{quote}\nCheers!,\nDeep"
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person_data["email"],
            msg=f"Subject:Happy Birthday\n\n{message}",
        )


# ---------------------------- VERIFY IF TODAY MATCHES WITH ANY BIRTHDAY IN LIST ------------------------------- #
today = dt.datetime.today()

for birthday in birthday_list:
    if birthday["month"] == today.month and birthday["day"] == today.day:
        send_email(birthday, quote)
