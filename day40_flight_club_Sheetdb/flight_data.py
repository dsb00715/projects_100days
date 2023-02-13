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

    def get_flight_info(self, dest_city, max_stopovers):
        endpoint = f"{TEQ_ENDPOINT}?fly_from={HOME_CITY}&fly_to={dest_city}&date_from={TOMORROW}&date_to={LAST_DATE}&nights_in_dst_from=4&nights_in_dst_to=6&flight_type=round&adults=1&selected_cabins=M&curr=EUR&max_stopovers={max_stopovers}&sort=price&one_for_city=1"
        headers = {
            "accept": "application/json",
            "apikey": TEQ_API_KEY,
        }
        response = get(url=endpoint, headers=headers)
        return response

    def get_flight_data(self, dest_city):
        response = self.get_flight_info(dest_city, 0)
        try:
            data = response.json()["data"][0]
        except IndexError:
            response = self.get_flight_info(dest_city, 2)
            data = response.json()["data"][0]
        finally:
            return data
