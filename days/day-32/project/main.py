import smtplib
import datetime as dt
import random


def send_email(email, email_password, receiver_email, message):
    """
    Sends an email
    """
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=email_password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver_email,
            msg=f"Subject:Motivational Quote\n\n{message}"
        )


def get_quote():
    """
    Gets a random quote from the quotes.txt file
    """

    with open("quotes.txt", "r") as quotes_data:
        quotes = quotes_data.readlines()
        quote = random.choice(quotes)
    return quote


email = ""
password = ""
to_email = ""
motivational_quote = get_quote()

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 0:
    send_email(email=email, email_password=password,
               receiver_email=to_email, message=motivational_quote)
