import requests
from datetime import datetime
import smtplib
import time

MY_LAT = -26.204103 # Your latitude
MY_LONG = 28.047304 # Your longitude
email = ""
password = ""
to_email = ""

#If the ISS is close to my current position
def is_iss_overhead():
    print("API calling 1")
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print("checking location")
    return abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5

#Your position is within +5 or -5 degrees of the ISS position.


# and it is currently dark
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    print("API calling 2")
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    return time_now >= sunset or time_now <= sunrise 


# Then send me an email to tell me to look up.
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


# BONUS: run the code every 60 seconds.

while True:
    print("Start")
    time.sleep(60)
    if is_dark() and is_iss_overhead():
        send_email(email, password, to_email, "Subject:ISS Overhead\n\nLook up! \nISS Overhead!")

