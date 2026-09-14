# Notes

## How sending email works

### `sender - lesetja@gmail.com`, `recipient - timmy@yahoo.com`

- Gmail mail Server recieves the message, Yahoo Mail Server stores the message until the recipient logs in and gets the email
- This transfer relies on `smtp`

| Simple Mail Transfer Protocol

```python
import smtplib

email = "test@gmail.com" # testing email

connection = smtplib.SMTP("smtp.gmail.com") # connect email provider smtp server (gmail)
connection.starttls() # protocol that encrypts email messages
connection.login(user=email, password=password) # password from gmail app passwords
connection.sendmail(from_addr=email, to_addrs=to_email, msg="Hello, World!")
connection.close()
```

# Setup password in Gmail

- We go to Gmail -> Security -> App Passwords -> (setup app), click generate

# Working with dates and time

- We can access today's date data like below, and extract info from it

```python
now = dt.datetime.now() # current date and time
year = now.year # current year (int)

if year == 2026:
    print("Here we go")
day_of_the_week = now.weekday()
print(day_of_the_week)
print(now)
print(year)
```

### How to create our own date

```python
import datetime as dt

date_of_birth = dt.datetime(year=1995, month=3, day=12)
```