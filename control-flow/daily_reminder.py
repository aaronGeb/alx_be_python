#!/usr/bin/env python3
# personal daily reminder script
description = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        reminder = f"Reminder: '{description}' is a {priority} priority"
    case "medium" | "low":
        reminder = f"Note: '{description}' is a {priority} priority task."
        
if time_bound == "yes":
    reminder += " task that requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."
print(reminder)
