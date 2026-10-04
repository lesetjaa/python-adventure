from dotenv import load_dotenv
import os
from requests_cache import CachedSession
load_dotenv()


FLIGHTS_SEARCH_ENDPOINT = os.environ["FLIGHTS_SEARCH_ENDPOINT"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, session: CachedSession) -> None:
        self.session = session
        self._api_key = os.environ["SERPAPI_API_KEY"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time) -> dict:
        parameters = {
            "engine": "google_flights",
            "departure_id": origin_city_code,
            "arrival_id": destination_city_code,
            "outbound_date": from_time.strftime("%Y-%m-%d"),
            "return_date": to_time.strftime("%Y-%m-%d"),
            "type": "1",
            "adults": "1",
            "api_key": self._api_key,
        }

        response = self.session.get(FLIGHTS_SEARCH_ENDPOINT, params=parameters)
        data = response.json()
        return data
