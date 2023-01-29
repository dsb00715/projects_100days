import requests
from datetime import datetime

MY_LAT = 51.434406
MY_LONG = 6.762329

""" response = requests.get(url="http://api.open-notify.org/iss-now.json")

data = response.json()

print(data) """

# https://api.sunrise-sunset.org/json

parameter = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now.hour)
