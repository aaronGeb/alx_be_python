#!/usr/bin/env python3
import datetime

def display_current_datetime():
    """Display the current date and time."""
    current_time = datetime.datetime.now()
    print(f"Current date and time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
def calculate_future_date(days):
    """Calculate the date after a given number of days."""
    future_date = datetime.datetime.now() + datetime.timedelta(days=days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date:"))
    calculate_future_date(days)
    