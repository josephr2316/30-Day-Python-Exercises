### Dates ###

# import datetime
from datetime import datetime

# function
def print_date(date):
    print(date)
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)   
    print(date.timestamp())

# Inicialize the date with the current time
now = datetime.now()


# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

print_date(now)
timestamp = now.timestamp()
print(timestamp)

year_2024 = datetime(2024, 1, 1) # Need to be included year, month and day, 
print(year_2024)
print_date(year_2024)

# year_2024 = datetime(2024) # TypeError: function missing required argument 'month' (pos 2)
# year_2024 = datetime(2024, 1) # TypeError: function missing required argument 'day' (pos 3)

#import time from module datetime
from datetime import time

current_time = time()
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

current_time = time(21, 6, 0)
print(current_time)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

currect_date = date.today()

print(currect_date.year)
print(currect_date.month)
print(currect_date.day)

currect_date = date(2023, 8, 16)
print(currect_date)
print(currect_date.year)
print(currect_date.month)
print(currect_date.day)
# currect_date.year += 1
# currect_date.year = currect_date.year + 1

currect_date = date(currect_date.year + 1, currect_date.month + 1, currect_date.day + 1)
print(currect_date)

# print(year_2024 - currect_date)
# print(year_2024.date - currect_date)

# diff = year_2024.date - currect_date
# diff = year_2024.date - currect_date
diff = year_2024 - now # Same type
diff = year_2024.date() - currect_date # Same type
diff = year_2024.time - current_time



from datetime import timedelta

time_delta = timedelta()

