import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import smtplib
import os

load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
RECIEVER_EMAIL = os.environ["RECIEVER_EMAIL"]
SMPT_ADDRESS = os.environ["SMPT_ADDRESS"]
ACCEPT_LANGUAGE = os.environ["ACCEPT_LANGUAGE"]
USER_AGENT = os.environ["USER_AGENT"]


URL = "https://www.amazon.co.za/Sony-WH-1000XM6-Headphones-Microphones-Studio-Quality/dp/B0F3PQHWTZ/ref=cs_sr_dp_2?crid=31WW137SBCMHH&dib=eyJ2IjoiMSJ9.G6fW22-sksvlrv2CemSOkdCDvOilr-FWrpPy48cYA1xypln1SrmA0FP-A3xy0eKpW04609_Gfle0HmZ_0UYkKYvGFf5X4VAyx1ky4fk1PAPc2ci1SAXGsTvvJQO6dYa0jQVURqf4QHpGv6xgEBnuWyacK29gi2IojwV6dHhxtMFG0fOn5iWCq-tjnxoDFHcfhM8ei7VFvXdqk-1IOfXZsQwymNJhBOJGDu57UEnBXm3aD1uSemwkeuRb1n8uqna1mnyOi7bCBt3wNLZOUjSQsWU5tEapL1kFkkB3OYzpLXk.Fv__I9rxm4rZQkdrGg2SzZQaTp6atp_BZa3Mq2KI-rw&dib_tag=se&keywords=Sony%2BWH-1000XM6&qid=1795173744&sprefix=sony%2Bwh-1000xm6%2Caps%2C569&sr=8-3&th=1"
headers = {
    "User-Agent": USER_AGENT,
    "ACCEPT_LANGUAGE": ACCEPT_LANGUAGE
}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()

html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

price_element = soup.find(name="span", class_="a-offscreen")
assert price_element is not None
print("Item Found!\n")
price = float(price_element.get_text().split("R")[1].replace(",", "").replace("\xa0", ""))


# TODO - Get Title
item_title = soup.find(name="span", id="productTitle").get_text().strip() # type: ignore
print(f"Item Title: {item_title}\n")

# TODO - Get Current Price
item_current_price = f"R{price}"

# TODO - Get Link
item_link = URL
print(f"Item Link: {item_link}\n")

message = f"Subject:AMAZON PRICE ALERT!!\n\n{item_title}\nis now at {item_current_price}\nLink: {item_link}"


def send_email(email, password, to_email):
    with smtplib.SMTP(SMPT_ADDRESS, port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            msg=message,
            from_addr=EMAIL,
            to_addrs=to_email
        )
        print("Email Sent!")


if float(item_current_price.split("R")[1]) < float(4100):
    send_email(EMAIL, PASSWORD, RECIEVER_EMAIL)
