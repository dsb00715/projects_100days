import requests
from twilio.rest import Client
import os

API_KEY = os.getenv("OWM_API_KEY")
MY_LAT = "51.401230"
MY_LONG = "6.768980"
OWM_API = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = "AC1e135815ad48c937fdc431effbb0cc74"
auth_token = os.getenv("AUTH_TOKEN")


def send_SMS():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella☔☔",
        from_="+18138562830",
        to="+4917657938425",
    )
    print(message.status)


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}
response = requests.get(url=OWM_API, params=parameters)
response.raise_for_status()
weather_data = response.json()

hourly_data = weather_data["hourly"][slice(0, 12)]  # or weather_data["hourly"][:12]
hourly_codes = []

for weather_data in hourly_data:
    hourly_codes.append(weather_data["weather"][0]["id"])

if any(
    val < 700 for val in hourly_codes
):  # to check if any list element match condition.
    # send_SMS()
    print("it's going to rain!")
