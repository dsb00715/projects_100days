from requests import get, put, post
from json import loads

USER_NAME = "ed24aedb42a2e06ab80f270e6509f4af"
PROJ_NAME = "flightDeals"
SHEET_NAME = "prices"
SHEET_USER = "dsb00715"
SHEET_PASS = "ebFQ9HpqoQ4OpYdVvVON"
SHEET_ENDPOINT = f"https://api.sheety.co/{USER_NAME}/{PROJ_NAME}/{SHEET_NAME}"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.data_set = {}

    def get_data(self):
        response = get(url=SHEET_ENDPOINT, auth=(SHEET_USER, SHEET_PASS))
        print(response.raise_for_status())
        data = response.json()
        self.data_set = data["prices"]
        return self.data_set

    def update_iata_code(self):
        for city in self.data_set:
            put_endpoint = f"{SHEET_ENDPOINT}/{city['id']}"
            data = {"price": {"iataCode": city["iataCode"]}}
            response = put(url=put_endpoint, json=data, auth=(SHEET_USER, SHEET_PASS))
            # print(response.text)
