from requests import *
import datetime as dt
import json
import os

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
USERNAME = os.getenv("USERNAME")
PROJECT_NAME = os.getenv("PROJECT_NAME")
SHEET_NAME = os.getenv("SHEET_NAME")
USER_NAME_SHEET = os.getenv("USER_NAME_SHEET")
PASS_SHEET = os.getenv("PASS_SHEET")


def save_data(api_data, time):
    for exercise in api_data["exercises"]:
        endpoint = f"https://api.sheety.co/{USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"
        data = {
            "workout": {
                "date": time.strftime("%d/%m/%Y"),
                "time": time.strftime("%H:%M:%S"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"],
            }
        }
        response = post(url=endpoint, json=data, auth=(USER_NAME_SHEET, PASS_SHEET))
        print(response.text)


def get_calories(user_input):
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    parameters = {"query": user_input}
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "dsb00715",
    }
    now = dt.datetime.now()
    response = post(url=endpoint, json=parameters, headers=headers)
    data = json.loads(response.text)
    save_data(api_data=data, time=now)


user_input = input("Tell me which exercises you did?")
get_calories(user_input=user_input)
