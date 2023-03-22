# https://www.amazon.de/-/en/Nutrition-Standard-Supplements-Glutamine-packaging/dp/B002DYIZH6/ref=nav_ya_signin?crid=3BYN97LKHC9JS&keywords=whey%2Bprotein&qid=1678468973&rdc=1&sprefix=whey%2Bprotien%2Caps%2C106&sr=8-5&th=1
from bs4 import BeautifulSoup
from os import environ, getenv
import requests
import smtplib


EMAIL = getenv("EMAIL")
PASSWORD = getenv("PASSWORD")
URL = "https://www.amazon.de/-/en/Nutrition-Standard-Supplements-Glutamine-packaging/dp/B002DYIZH6/ref=nav_ya_signin?crid=3BYN97LKHC9JS&keywords=whey%2Bprotein&qid=1678468973&rdc=1&sprefix=whey%2Bprotien%2Caps%2C106&sr=8-5&th=1"
HEADERS = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
}


def send_email(price, name):
    message = f"{name} is €{price}\n{URL}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="dsb00715@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8"),
        )


response = requests.get(url=URL, headers=HEADERS)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "lxml")
price_tags = soup.find_all(
    name="div",
    class_="a-column a-span12 a-text-left",
)
product_name = (
    soup.find(name="span", class_="a-size-large product-title-word-break").text
).strip()
for tag in price_tags:
    if tag.find(name="span", class_="a-offscreen"):
        price_v = tag.find(name="span", class_="a-offscreen")
        product_price = price_v.text.split("€")[1]
        if float(product_price) < 36:
            send_email(product_price, product_name)
        else:
            print("Price is still above/at last price.")
    break
