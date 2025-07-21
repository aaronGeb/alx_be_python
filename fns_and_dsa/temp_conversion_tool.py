#!/usr/bin/env python3
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
user_input = float(input("Enter the temperature to convert:"))
temperature = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if temperature == "C":
    converted = convert_to_fahrenheit(user_input)
    print(f"{user_input}°C is {converted}°F")
elif temperature == "F":
    converted = convert_to_celsius(user_input)
    print(f"{user_input}°F is {converted}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
