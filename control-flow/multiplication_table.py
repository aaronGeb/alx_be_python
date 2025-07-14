#!/usr/bin/env python3
# multiplication table generator
number = int(input("Enter a number to generate its multiplication table: "))

for i in range(1, 11):
    print(f"{number} * {i}= {number * i}")
