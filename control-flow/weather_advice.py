#!/usr/bin/env python3
# weather advice based on conditions
weather = input("What's the weather like today?").lower()
if weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
