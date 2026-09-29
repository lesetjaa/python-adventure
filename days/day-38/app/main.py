import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

WORKOUTS_URL = "https://app.100daysofpython.dev"

API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
USERNAME = os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
PASSWORD = os.environ["PASSWORD"]


workout_req_config = {
    "query": input("Tell me which exercise you did: "),
}

workout_req_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}


calc_calory_endpoint = f"{WORKOUTS_URL}/v1/nutrition/natural/exercise"
sheet_endpoint = SHEET_ENDPOINT

workouts = requests.post(url=calc_calory_endpoint,
                         headers=workout_req_header, json=workout_req_config)
print(workouts.text)

exercises = workouts.json()["exercises"]

todays_date = datetime.now()
for exercise in exercises:

    workout = {
        "workout": {
            "date": todays_date.strftime("%d/%m/%Y"),
            "time": todays_date.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    # for basic auth
    # response2 = requests.post(url=sheet_endpoint, json=workout, auth=("lesetja", PASSWORD))

    # for bearer (token) auth
    bearer_header = {
        "Authorization": f"Bearer {TOKEN}"
    }
    response2 = requests.post(url=sheet_endpoint, json=workout, headers=bearer_header)

    print(response2.text)
