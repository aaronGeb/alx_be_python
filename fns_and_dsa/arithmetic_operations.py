#!/usr/bin/env python3


def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operations based on the provided operation type.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
        float: The result of the arithmetic operation.

    Raises:
        ValueError: If an unsupported operation is provided.
    """
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            return num1 / num2
        case _:
            raise ValueError(f"Unsupported operation: {operation}")
