from requests import get, put, post
from json import loads

SHEET_ENDPOINT = "https://sheetdb.io/api/v1/be2wved2919pg"
SHEET_USER = "ql6kxdrm"
SHEET_PASS = "6g69nrm52g5tpmxxtvql"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        self.data_set = {}
        self.user_info = {}

    def get_data(self):
        response = get(url=SHEET_ENDPOINT, auth=(SHEET_USER, SHEET_PASS))
        self.data_set = response.json()
        return self.data_set

    def update_iata_code(self):
        for city in range(len(self.data_set)):
            put_endpoint = f"{SHEET_ENDPOINT}/City/{self.data_set[city]['City']}"
            data = {"IATA Code": self.data_set[city]["IATA Code"]}
            response = put(url=put_endpoint, json=data, auth=(SHEET_USER, SHEET_PASS))
            response.raise_for_status()
            # print(response.text)

    def get_user_info(self):
        user_endpoint = f"{SHEET_ENDPOINT}?sheet=users"
        response = get(url=user_endpoint, auth=(SHEET_USER, SHEET_PASS))
        self.user_info = response.json()
        return self.user_info


""" 
# Sheety
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
            # print(response.text) """
