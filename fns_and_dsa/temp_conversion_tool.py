#!/usr/bin/env python3
# -- coding: utf-8 -*-
"""Temperature Conversion Tool"""
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp = float(input("Enter the temperature to convert:"))
    unit = (
        input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    )
    if unit == "C":
        print(f"{temp}\u00B0C is {celsius_to_fahrenheit(temp)}\u00B0F")
    elif unit == "F":
        print(f"{temp}\u00B0F is {convert_to_celsius(temp)}\u00B0C.")
    else:
        print("Invalid unit entered.")


if __name__ == "__main__":
    main()
