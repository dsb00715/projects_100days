import os
from requests import post

SHEET_ENDPOINT = "https://sheetdb.io/api/v1/be2wved2919pg?sheet=users"
SHEET_USER = os.getenv("SHEET_USER")
SHEET_PASS = os.getenv("SHEET_PASS")

print("Welcome to Deep's Flight Club.")
print("We will find the best flight deals and email you.")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email id? ")
email_conf = input("Type your email again! ")
if email == email_conf:
    data = {
        "FirstName": first_name,
        "LastName": last_name,
        "Email": email,
    }
    try:
        response = post(url=SHEET_ENDPOINT, json=data, auth=(SHEET_USER, SHEET_PASS))
        print("You're in the club")
    except:
        response.raise_for_status()
else:
    print("Make sure to type same email id twice!")
