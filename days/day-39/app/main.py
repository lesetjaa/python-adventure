# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import FlightData, find_cheapest_flight
from notification_manager import NotificationManager

ORIGIN_CITY = "JNB"

session = requests_cache.CachedSession('cache', expire_after=3600)


tomorrow = datetime.today() + timedelta(days=1)
six_month_from_today = datetime.today() + timedelta(weeks=4*6)

data = DataManager(session=session)
sheet_data = data.get_flights()


find_flights = FlightSearch(session=session)
current_flight = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
for destination in sheet_data:
    all_flights = find_flights.check_flights(
        origin_city_code=ORIGIN_CITY,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(all_flights, return_date=six_month_from_today)

    if cheapest_flight.price == "N/A":
        continue

    if current_flight.price == "N/A" or cheapest_flight.price < current_flight.price:
        current_flight = cheapest_flight

notification = NotificationManager()
if current_flight.price != "N/A":
    message = f"Lowest Price Alert! Only ${current_flight.price} to Fly from {current_flight.origin_airport} to {current_flight.destination_airport}, on {current_flight.out_date} until {current_flight.return_date}."
    notification.send_SMS(message=message)

