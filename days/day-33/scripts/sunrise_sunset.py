import requests
from datetime import datetime

# Johannesburg
LATITUDE = -26.204103
LONGITUDE = 28.047304

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,  # return with unformatted time
}  # Johannesburg

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)

data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # get hour
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
