# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# a1tTqGjjHpfgKhmUp-_3ar9_Y7b5L4QC
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

excel_data = data_manager.get_data()

for city in excel_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.get_iata_code(city["city"])
data_manager.data_set = excel_data
data_manager.update_iata_code()

for city in excel_data:
    data_for_flight = flight_data.get_flight_data(dest_city=city["iataCode"])
    if city["lowestPrice"] > data_for_flight["price"]:
        notification_manager.send_email(data_for_flight)
