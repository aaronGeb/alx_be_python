#!/usr/bin/env python3
# personal daily reminder script
task = input("Enter your task:")
priority = input("Priority (high, medium, low):")
time_bound = input("Is it time bound (yes or no):")
match priority.lower():
    case "high":
        reminder = f"Reminder: {task} is a high priority task"
    case "medium":
        reminder = f"Reminder: {task} is a medium priority task"
    case "low":
        reminder = f"Reminder: {task} is a low priority task"
    case _:
        reminder = f"Reminder: {task} has an unknown priority."
        
if time_bound.lower() == "yes":
    reminder += " This task requires immediate attention today!"
elif time_bound.lower() == "no":
    reminder += ". Consider completing it when you have free time"
print(reminder)
