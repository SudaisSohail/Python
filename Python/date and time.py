import datetime as dt
import pytz

# dt.date(Y, M, D)
# dt.time(h, m, s, ms)
# dt.datetime(Y, M, D, h, m, s, ms)


today = dt.date.today()    # Today's date

print(today)

print(today.month)  # prints current month

print(today.day)

print(today.weekday())  # It starts counting from 0 so it returns 1 less 

print(today.isoweekday())  # It starts counting from 1 not from 0

birthday = dt.date(2006, 2, 16)     # My birthdate
print(birthday)

days_since_birth = (today - birthday).days      # .days returns answer in days
print(days_since_birth)

tdelta = dt.timedelta(days = 10)     # To add or subtract days from a date
print(today + tdelta)

print(dt.time(5, 39, 49, 29))       # Returns a datetime object

# Add 12 hours to current day
hour_delta = dt.timedelta(hours = 12)
print(dt.datetime.now() + hour_delta)

datetime_today = dt.datetime.now(tz = pytz.UTC)
datetime_GMT = datetime_today.astimezone(pytz.timezone("GMT"))
print(datetime_GMT)

for tz in pytz.all_timezones:
    #print(tz)
    pass

# string formatting with dates
# 2021-10-01 -> October 1, 2021
# strftime (f = formatting)

print(datetime_GMT.strftime("%B %d, %Y"))  # B=month, d=date, Y=year

# October 1, 2021 -> datetime(2021, 19, 1)
# strptime (p = parsing)

print(dt.datetime.strptime("October 01, 2021", "%B %d, %Y"))


