from requests import get
import datetime as dt

TEQ_API_KEY = "a1tTqGjjHpfgKhmUp-_3ar9_Y7b5L4QC"
TEQ_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
HOME_CITY = "DUS"
TOMORROW = (dt.datetime.today() + dt.timedelta(days=1)).strftime("%d/%m/%Y")
LAST_DATE = (dt.datetime.today() + dt.timedelta(days=180)).strftime("%d/%m/%Y")


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self) -> None:
        self.data = {}

    def get_flight_data(self, dest_city):
        endpoint = f"{TEQ_ENDPOINT}?fly_from={HOME_CITY}&fly_to={dest_city}&date_from={TOMORROW}&date_to={LAST_DATE}&nights_in_dst_from=4&nights_in_dst_to=6&flight_type=round&adults=2&selected_cabins=M&curr=EUR&max_stopovers=0&sort=price"
        headers = {
            "accept": "application/json",
            "apikey": TEQ_API_KEY,
        }
        response = get(url=endpoint, headers=headers)
        data = response.json()
        if len(data["data"]) != 0:
            # price = data["data"][0]["price"]
            # dept_city = data["data"][0]["cityFrom"]
            # dept_airport = data["data"][0]["route"][0]["flyFrom"]
            # arrival_city = data["data"][0]["cityTo"]
            # arrival_airport = data["data"][0]["route"][0]["flyTo"]
            # out_date = data["data"][0]["route"][0]["local_departure"].split("T")
            # in_date = data["data"][0]["route"][1]["local_arrival"].split("T")
            data_from_flight = data["data"][0]
            # print(f"{dest_city}: €{self.price}")
            return data_from_flight
