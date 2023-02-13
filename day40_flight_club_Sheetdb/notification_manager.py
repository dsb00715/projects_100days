import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        pass

    def send_email(self, data, user_data):
        for user in user_data:
            first_name = user["FirstName"]
            user_email = user["Email"]
            price = data["price"]
            city_from = data["cityFrom"]
            airport_from = data["route"][0]["flyFrom"]
            city_to = data["cityTo"]
            airport_to = data["route"][0]["flyTo"]
            outbound_date = data["route"][0]["local_departure"].split("T")[0]
            inbound_date = data["route"][1]["local_arrival"].split("T")[0]
            link = data["deep_link"]

            message = MIMEMultipart()
            message["Subject"] = f"Flight to {data['cityTo']} is cheaper!!!"
            message["From"] = EMAIL
            message["To"] = user_email
            if len(data["route"]) == 2:
                msg = """\
                <html>
                    <head>Dear {first_name},</head>
                    <body>
                        <p>Low price alert!!<br>
                            only €{price} to fly from {city_from}-{airport_from} to {city_to}-{airport_to},<br>
                            from {outbound_date} to {inbound_date}.<br>
                            Here is the <a href={link}>link</a> to book tickets.
                        </p>
                    </body>
                    <head>Have a nice day ahead!<br>Best Regards,<br>Deep's Flight Club Team</head>
                </html>
                """.format(
                    **locals()
                )
            elif len(data["route"]) >= 4:
                airport_to = data["route"][1]["flyTo"]
                inbound_date = data["route"][2]["local_arrival"].split("T")[0]
                stop_over = data["route"][1]["cityFrom"]
                msg = """\
                <html>
                    <head>Dear {first_name},</head>
                    <body>
                        <p>Low price alert!!<br>
                            only €{price} to fly from {city_from}-{airport_from} to {city_to}-{airport_to},<br>
                            from {outbound_date} to {inbound_date}.<br>
                            Flight has 1 stop over, via {stop_over} city.<br>
                            Here is the <a href={link}>link</a> to book tickets.
                        </p>
                    </body>
                    <head>Have a nice day ahead!<br>Best Regards,<br>Deep's Flight Club Team</head>
                </html>
                """.format(
                    **locals()
                )
            message.attach(MIMEText(msg, "html"))

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(EMAIL, user_email, message.as_string())
