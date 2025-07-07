#!/usr/bin/env python3
# personal finance calculator

monthly_income = int(input("Enter your monthly income: "))  # get monthly income
monthly_exp = int(input("Enter your monthly expenses:"))

monthly_savings = monthly_income - monthly_exp  # calculate monthly savings
annual_savings = monthly_savings * 12 + (
    monthly_savings * 12 * 0.05
)  # calculate annual savings
print(f"Your monthly savings are: ${monthly_savings}.")
print(f"Projected saving after onr year, with interest, is: ${int(annual_savings)}.")
