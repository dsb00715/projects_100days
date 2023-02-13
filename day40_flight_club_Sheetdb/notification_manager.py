import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL = "testgetesten@gmail.com"
PASSWORD = "wmdoeffzjfuabjcg"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    # def send_email(self, data, user_data):
    #     link = MIMEText(
    #         """<a href="{data_link}">click here to book your tickets</a>""".format(
    #             data_link=data["deep_link"]
    #         ),
    #         "html",
    #     )
    #     # link = data["deep_link"]
    #     if len(data["route"]) == 2:
    #         message = f"Low price alert!!\nonly €{data['price']} to fly from {data['cityFrom']}-{data['route'][0]['flyFrom']} to {data['cityTo']}-{data['route'][0]['flyTo']},\nfrom {data['route'][0]['local_departure'].split('T')[0]} to {data['route'][1]['local_arrival'].split('T')[0]}\n{link}"
    #     elif len(data["route"]) >= 4:
    #         message = f"Low price alert!!\nonly €{data['price']} to fly from {data['cityFrom']}-{data['route'][0]['flyFrom']} to {data['cityTo']}-{data['route'][1]['flyTo']},\nfrom {data['route'][0]['local_departure'].split('T')[0]} to {data['route'][2]['local_arrival'].split('T')[0]}\nFlight has 1 stop over, via {data['route'][1]['cityFrom']} city.\n{link}"

    #     with smtplib.SMTP("smtp.gmail.com") as connection:
    #         connection.starttls()
    #         connection.login(user=EMAIL, password=PASSWORD)
    #         print(data["price"])
    #         for user in user_data:
    #             connection.sendmail(
    #                 from_addr=EMAIL,
    #                 to_addrs=user["Email"],
    #                 msg=f"Subject:Flight to {data['cityTo']} is cheaper!!!\n\nDear {user['FirstName']},\n{message}".encode(
    #                     "utf-8"
    #                 ),
    #             )

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
                # message = f"Low price alert!!\nonly €{data['price']} to fly from {data['cityFrom']}-{data['route'][0]['flyFrom']} to {data['cityTo']}-{data['route'][0]['flyTo']},\nfrom {data['route'][0]['local_departure'].split('T')[0]} to {data['route'][1]['local_arrival'].split('T')[0]}\n{link}"
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
                # message = f"Low price alert!!\nonly €{data['price']} to fly from {data['cityFrom']}-{data['route'][0]['flyFrom']} to {data['cityTo']}-{data['route'][1]['flyTo']},\nfrom {data['route'][0]['local_departure'].split('T')[0]} to {data['route'][2]['local_arrival'].split('T')[0]}\nFlight has 1 stop over, via {data['route'][1]['cityFrom']} city.\n{link}"

            message.attach(MIMEText(msg, "html"))

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(EMAIL, user_email, message.as_string())
