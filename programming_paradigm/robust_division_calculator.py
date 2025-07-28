#!/usr/bin/env python3
"""Robust Division Calculator"""


def safe_divide(numerator, denominator):
    """Safe division with error handling."""
    try:
        num = float(numerator)
        denom = float(denominator)
        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return f"The result of the division is {num / denom}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError as e:
        return str(e)
    except Exception as e:
        return f"An unexpected error occurred: {e}"
