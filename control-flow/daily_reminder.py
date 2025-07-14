#!/usr/bin/env python3
# personal daily reminder script
description = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    reminder = f"Reminder: {description} is a {priority} priority"
    case "high":
      if time_bound == "yes":
          reminder += " task that requires immediate attention!"
      elif time_bound == "no":
          reminder += ". Consider completing it when you have free time"
          
    case "medium" | "low":
      if time_bound.lower() == "yes":
            reminder += " This description requires immediate attention today!"
      elif time_bound.lower() == "no":
            reminder += ". Consider completing it when you have free time"
   
print(reminder)
