FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


def convert_to_celsius(temprature):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    celsius = (temprature - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{temprature}°F is {celsius}°C")

def convert_to_(temprature):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (temprature - 32) * CELSIUS_TO_FAHRENHEIT_FACTOR
    print(f"{temprature}°F is {fahrenheit}°C")


temprature = float(input("Enter the temperature to convert: "))
conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if conversion == "F":
    convert_to_celsius(temprature)
elif conversion == "C":
    convert_to_(temprature)
else:
    print("Invalid input")

