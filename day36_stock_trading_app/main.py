import requests
import datetime as dt
from math import ceil
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_ACCESS_KEY = os.getenv("ALPHA_ACCESS_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
account_sid = "AC1e135815ad48c937fdc431effbb0cc74"
auth_token = os.getenv("AUTH_TOKEN")
final_news = []

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stocks_info():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={STOCK}&interval=60min&apikey={ALPHA_ACCESS_KEY}"
    r = requests.get(url)
    stocks_data = r.json()
    # To get only time series data from whole json
    hourly_data = stocks_data["Time Series (60min)"]
    # Splits dictionary into just 2 days of data
    last_day_data = dict(list(hourly_data.items())[: len(hourly_data) // 5])
    final_stocks = [v["4. close"] for k, v in last_day_data.items() if "20:00:00" in k]
    return (
        (float(final_stocks[0]) - float(final_stocks[1])) / float(final_stocks[0])
    ) * 100


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    final_news_dict = {}
    news_url = f"https://newsapi.org/v2/everything?q={STOCK}&apiKey={NEWS_API_KEY}&pageSize=3&page=1&source=us"
    r = requests.get(news_url)
    data = r.json()
    articles = data["articles"]
    for article in articles:
        final_news_dict["Headline"] = article["title"]
        final_news_dict["Brief"] = article["description"]
        final_news.append(final_news_dict)
        final_news_dict = {}
    return final_news


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
def send_sms(stock_difference, news_headline, news_brief):
    client = Client(account_sid, auth_token)
    if stock_difference > 0:
        msg = f"{COMPANY_NAME}: 🔺{stock_difference}%\nHeadline: {news_headline}\nBrief: {news_brief}"
    else:
        msg = f"{COMPANY_NAME}: 🔻{stock_difference}%\nHeadline: {news_headline}\nBrief: {news_brief}"
    message = client.messages.create(
        body=msg,
        from_="+18138562830",
        to="+4917657938425",
    )
    print(message.status)


difference = get_stocks_info()
if difference >= 5 or difference <= -5:
    news_articles = get_news()
    for article in news_articles:
        send_sms(
            stock_difference=ceil(difference),
            news_headline=article["Headline"],
            news_brief=article["Brief"],
        )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
