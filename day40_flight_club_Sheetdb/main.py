# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

excel_data = data_manager.get_data()
user_info = data_manager.get_user_info()

for city in excel_data:
    if city["IATA Code"] == "":
        city["IATA Code"] = flight_search.get_iata_code(city["City"])
data_manager.data_set = excel_data
data_manager.update_iata_code()

for city in excel_data:
    data_for_flight = flight_data.get_flight_data(dest_city=city["IATA Code"])
    if data_for_flight is None:
        continue
    if int(city["Lowest Price"]) > data_for_flight["price"]:
        notification_manager.send_email(data=data_for_flight, user_data=user_info)
        print("email sent")
