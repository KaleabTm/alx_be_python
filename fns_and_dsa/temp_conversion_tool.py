# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Function to validate numeric input for temperature
def get_temperature_input():
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

# Main program
def temperature_conversion():
    # Get the temperature from the user
    temperature = get_temperature_input()

    # Get the unit (Celsius or Fahrenheit) from the user
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'F':
        # Convert from Fahrenheit to Celsius
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temperature}°C.")
    elif unit == 'C':
        # Convert from Celsius to Fahrenheit
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temperature}°F.")
    else:
        print("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")

# Call the main function to start the temperature conversion tool
temperature_conversion()
