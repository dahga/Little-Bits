import datetime
import time

# Get user input for the date and time of the event
event_year = int(input("Enter the year of the event: "))
event_month = int(input("Enter the month of the event (1-12): "))
event_day = int(input("Enter the day of the event (1-31): "))
event_hour = int(input("Enter the hour of the event (0-23): "))
event_minute = int(input("Enter the minute of the event (0-59): "))
event_second = int(input("Enter the second of the event (0-59): "))

# Calculate the time remaining until the event
event_time = datetime.datetime(event_year, event_month, event_day, event_hour, event_minute, event_second)
current_time = datetime.datetime.now()
time_remaining = event_time - current_time

# Start the countdown
while time_remaining.total_seconds() > 0:
    days, remainder = divmod(time_remaining.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    print("Time remaining until the event: {:02d} days, {:02d} hours, {:02d} minutes, {:02d} seconds".format(
        int(days), int(hours), int(minutes), int(seconds)))
    time.sleep(1)
    current_time = datetime.datetime.now()
    time_remaining = event_time - current_time

print("Event time has arrived!")
