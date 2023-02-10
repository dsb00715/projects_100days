import smtplib


EMAIL = "testgetesten@gmail.com"
PASSWORD = "wmdoeffzjfuabjcg"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(person_data, data):
        price = data["price"]
        dept_city = data["cityFrom"].encode("utf-8")
        dept_airport = data["route"][0]["flyFrom"]
        arrival_city = data["cityTo"]
        arrival_airport = data["route"][0]["flyTo"]
        out_date = data["route"][0]["local_departure"].split("T")[0]
        in_date = data["route"][1]["local_arrival"].split("T")[0]

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            message = f"Low price alert!!\nonly €{price}to fly from{dept_city}-{dept_airport} to {arrival_city}-{arrival_airport}, from {out_date} to {in_date}"
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs="dsb00715@gmail.com",
                msg=f"Subject:Flight to {arrival_city}-{arrival_airport} is cheaper!!!\n\n{message}",
            )
