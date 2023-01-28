""" import smtplib

my_mail = "testgetesten@gmail.com"
my_pass = "wmdoeffzjfuabjcg"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=my_pass)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="dsb00715@gmail.com",
        msg="Subject:Hello\n\nThis is the body of the email",
    )
 """

""" import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()

print(day_of_week) """
import datetime as dt
import smtplib
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open(r"day32_SMTPlib_email\quotes.txt") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

my_mail = "testgetesten@gmail.com"
my_pass = "wmdoeffzjfuabjcg"
message = random.choice(lines)

if day_of_week == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=my_pass)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs="dsb00715@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{message}",
        )
