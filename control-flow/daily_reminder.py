#!/usr/bin/env python3
# personal daily reminder script
description = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        reminder = f"Reminder: {description} is a high priority description"
    case "medium" | "low":
        reminder = f"Note: {description} is a medium priority description"
        
if time_bound.lower() == "yes":
    reminder += " This description requires immediate attention today!"
elif time_bound.lower() == "no":
    reminder += ". Consider completing it when you have free time"
print(reminder)
