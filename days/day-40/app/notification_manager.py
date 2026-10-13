import os
from vonage import Auth, Vonage
from vonage_messages import Sms
import smtplib
from twilio.rest import Client

# Using a .env file to retrieve the phone numbers and tokens.
EMAIL = os.environ["FROM_EMAIL"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]


class NotificationManager:

    # def __init__(self):
    #     self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
    #     self.email = os.environ["MY_EMAIL"]
    #     self.email_password = os.environ["MY_EMAIL_PASSWORD"]
    #     self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
    #     self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"])

    def __init__(self) -> None:
        self.VONAGE_API_KEY = os.environ["VONAGE_API_KEY"]
        self.VONAGE_SECRET_KEY = os.environ["VONAGE_SECRET_KEY"]
        self.MY_NUMBER = os.environ["MY_NUMBER"]
        self.FROM_NUMBER = os.environ["FROM_NUMBER"]
        self.client = Vonage(
            Auth(api_key=self.VONAGE_API_KEY, api_secret=self.VONAGE_SECRET_KEY))

    def send_SMS(self, message):
        response = self.client.messages.send(
            Sms(
                to=self.MY_NUMBER,
                from_=self.FROM_NUMBER,
                text=message
            )  # type: ignore
        )
        print(response)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    # def send_whatsapp(self, message_body):
    #     message = self.client.messages.create(
    #         from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
    #         body=message_body,
    #         to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
    #     )
    #     print(message.sid)

    def send_email(self, to_email, message):
        print("sending message")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=to_email,
                msg=message)
            print("Email sent")
