from datetime import datetime, timedelta 

def display_current_datetime ():
    current_date = datetime.now()
    current_date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print (" Current date and time:" + current_date_formatted)


def calculate_future_date ():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_day = datetime.now()  + timedelta(days=number_of_days)
    future_date = future_day.strftime("%Y-%m-%d")
    print("Future day: " + future_date)

display_current_datetime()
calculate_future_date()