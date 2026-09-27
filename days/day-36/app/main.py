import smtplib

import requests_cache
import os
from dotenv import load_dotenv
import json
import os
# from twilio.rest import Client
from vonage import Auth, Vonage
from vonage_messages import Sms

# Load environment variables from the .env file
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
MY_NUMBER = os.getenv("MY_NUMBER")
FROM_NUMBER = os.getenv("FROM_NUMBER")

STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
# TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
# TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
VONAGE_API_KEY = os.environ["VONAGE_API_KEY"]
VONAGE_SECRET_KEY = os.environ["VONAGE_SECRET_KEY"]


def percentage_change(new_number, original_number):
    new_number = float(new_number)
    original_number = float(original_number)
    percentage = ((new_number - original_number) / original_number) * 100
    return round(percentage, 2)


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "searchIn": "title",
}

session = requests_cache.CachedSession('demo_cache', expire_after=3600)
response1 = session.get(STOCK_ENDPOINT, params=stock_parameters)
response1.raise_for_status()
stock_data = response1.json()

data_dates = list(stock_data["Time Series (Daily)"].values())

yesterdays_data = data_dates[0]
before_yesterdays_data = data_dates[1]

yesterday_close = yesterdays_data["4. close"]
before_yesterdays_close = before_yesterdays_data["4. close"]

difference_percentage = percentage_change(
    yesterday_close, before_yesterdays_close)
up_down = "🔺" if difference_percentage > 0 else "🔻"

if abs(difference_percentage) >= 5:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    response2 = session.get(NEWS_ENDPOINT, params=news_parameters)
    response2.raise_for_status()
    news_data = response2.json()["articles"]

    articles = news_data[:3]

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

    formatted_articles = [
        f"{STOCK}: {up_down}{difference_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}.\nDate: {article['publishedAt'].split("T")[0]}"
        for article in articles
    ]

    # STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    # Download the helper library from https://www.twilio.com/docs/python/install
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure

    # client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    # body = "\n\n".join(formatted_articles)
    # message = client.messages.create(
    #     to=str(MY_NUMBER),
    #     from_=FROM_NUMBER,
    #     body=formatted_articles,
    # )
    # print(formatted_articles)
    # print(message.sid)

    # Use Vongue instead.
    client = Vonage(Auth(api_key=VONAGE_API_KEY, api_secret=VONAGE_SECRET_KEY))

    response = client.messages.send(
        Sms(
            to=MY_NUMBER,
            from_=FROM_NUMBER,
            text=formatted_articles[0]
        )  # type: ignore
    )
    print(response)
