#!/usr/bin/env python3
# personal daily reminder script
description = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{description}' is a {priority} priority "
                  "task that requires immediate attention today!")
        else:
            print(f"Note: '{description}' is a {priority} priority task. "
                  "Consider completing it when you have free time.")
    case "medium" | "low":
            print(f"Note: '{description}' is a {priority} priority task. "
                  "Consider completing it when you have free time.")
