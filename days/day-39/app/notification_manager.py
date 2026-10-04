from vonage import Auth, Vonage
from vonage_messages import Sms
import os


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
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
