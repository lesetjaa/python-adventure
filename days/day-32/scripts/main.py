import datetime as dt

now = dt.datetime.now() # current date and time
year = now.year # current year (int)

if year == 2026:
    print("Here we go")
day_of_the_week = now.weekday()
print(day_of_the_week)
print(now)
print(year)

# Year, month, day are required
date_of_birth = dt.datetime(year=1995, month=3, day=12)
print(date_of_birth) # the rest are set to default