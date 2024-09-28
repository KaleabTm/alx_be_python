from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as 'YYYY-MM-DD HH:MM:SS'
    current_date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: " + current_date_formatted)

def calculate_future_date():
    # Prompt the user for the number of days to add
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=number_of_days)
    # Format the future date as 'YYYY-MM-DD'
    future_date_formatted = future_date.strftime("%Y-%m-%d")
    print("Future date: " + future_date_formatted)

# Call the functions
display_current_datetime()
calculate_future_date()
