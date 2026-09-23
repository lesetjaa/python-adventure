import requests
import os
import smtplib

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
TO_EMAIL = os.environ.get("TO_EMAIL")

LAT = os.environ.get("LAT")
LON = os.environ.get("LON")
API_KEY = os.environ.get("API_KEY")


def send_email(from_email, from_email_password, to_email, message):
    print("sending message")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_email_password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to_email,
            msg=message)
        print("Email sent")

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "cnt": 4, # 16 hours of data
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
print(f"Status Code: {response.status_code}")
data = response.json()


def get_weather_code(weather_data: dict) -> list:
    weather_list = weather_data["list"]
    weather_codes = []

    for weather in weather_list:
        weather_codes.append(weather["weather"][0]["id"])

    return weather_codes


codes = get_weather_code(data)
email_msg = "Subject:Rain Incoming\n\nIt might rain today, get an umbrella!"
for code in codes:
    if code < 700:
        send_email(MY_EMAIL, MY_PASSWORD, TO_EMAIL, message=email_msg)
        break