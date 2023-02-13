import os
from requests import get, put, post
from json import loads

TEQ_API_KEY = os.getenv("TEQ_API_KEY")
TEQ_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        pass

    def get_iata_code(self, city):
        endpoint = f"{TEQ_ENDPOINT}?term={city}&location_types=airport"
        headers = {
            "accept": "application/json",
            "apikey": TEQ_API_KEY,
        }
        response = get(url=endpoint, headers=headers)
        data = loads(response.text)
        iata_code = data["locations"][0]["city"]["code"]
        return iata_code
