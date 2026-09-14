##################### Extra Hard Starting Project ######################
import pandas
import smtplib
import datetime as dt
import random

email = ""
password = ""
to_email = ""


def get_random_letter():
    return f"templates/letter_{random.randint(1, 3)}.txt"


def send_email(from_email, from_email_password, to_email, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_email_password)
        connection.sendmail(
            from_addr=email,
            to_addrs=to_email,
            msg=message)
        print("Email sent")


def update_letter():
    letter_name = get_random_letter()
    with open(letter_name, "r") as letter:
        content = letter.read()
        updated_letter = "Subject:Happy Birthday\n\n" + \
            content.replace("[NAME]", person["name"])
    return updated_letter

# 1. Update the birthdays.csv
# Updated


now = dt.datetime.now()
day_of_the_month = now.day
todays_month = now.month

birthdays = pandas.read_csv("birthdays.csv")
birthdays_in_dict = birthdays.to_dict(orient="records")

for person in birthdays_in_dict:
    birthday_day = person["day"]
    birthday_month = person["month"]

    # 2. Check if today matches a birthday in the birthdays.csv
    if birthday_day == day_of_the_month and birthday_month == todays_month:

        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        updated_letter = update_letter()

        # 4. Send the letter generated in step 3 to that person's email address.
        send_email(
            from_email=email,
            from_email_password=password,
            to_email=to_email,
            message=updated_letter
        )
