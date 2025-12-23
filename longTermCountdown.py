#! python3
# For a long-term countdown, you can use timedelta objects to measure the number of days, hours, minutes,
#  and seconds until some point (a birthday? an anniversary?) in the future
import datetime, time

event = datetime.datetime(2023, 4, 25, 0, 0, 0)
print('waiting...')
while datetime.datetime.now() < event:
    time.sleep(1)
print('Happy birthday!!! WOHOOO')