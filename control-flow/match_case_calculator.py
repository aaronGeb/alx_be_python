#!/usr/bin/env python3
# match case calculator
#num1, num2 = map(int, input(" Enter the first number: and Enter the second number:").split())
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Choose the operation (+, -, *, /): ")
match operation:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2  }")
    case "/":
        if num2 != 0:
            print(f"The result is {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter +, -, *, or /.")
