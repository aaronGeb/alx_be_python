#!/usr/bin/env python3
# personal daily reminder script
task = input("Enter your task:")
priority = input("Priority (high, medium, low):")
time_bound = input("Is it time bound (yes or no):")
match priority:
    case "high":
        reminder = f"Reminder: {task} is a high priority task"
    case "medium" | "low":
        reminder = f"Note: {task} is a medium priority task"
        
if time_bound.lower() == "yes":
    reminder += " This task requires immediate attention today!"
elif time_bound.lower() == "no":
    reminder += ". Consider completing it when you have free time"
print(reminder)
