from dotenv import load_dotenv
import os
from requests_cache import CachedSession
from datetime import datetime, timedelta
load_dotenv()

SHEET_PRICES_ENDPOINT = os.environ["SHEET_PRICES_ENDPOINT"]


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, session: CachedSession) -> None:
        self.token = os.environ["TOKEN"]
        self.session = session

    # def edit_flight(self, code_id, new_data: dict):
    #     self.session.put(f"{SHEET_PRICES_ENDPOINT}/{code_id}", params=new_data)

    # def add_flight(self, new_data: dict):
    #     self.session.post(SHEET_PRICES_ENDPOINT, data=new_data)

    def get_flights(self):
        self.bearer_header = {
            "Authorization": f"Bearer {self.token}"
        }
        response = self.session.get(
            url=SHEET_PRICES_ENDPOINT,
            headers=self.bearer_header
        )
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
