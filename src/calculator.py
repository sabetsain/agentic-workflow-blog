"""
Calculator module providing basic arithmetic operations.

This module implements a simple calculator with support for addition,
subtraction, multiplication, and division operations.
"""


def add(a, b):
    """
    Add two numbers.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number.

    Args:
        a (int or float): Numerator
        b (int or float): Denominator

    Returns:
        float: Quotient of a and b

    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operation, a, b):
    """
    Perform a calculation based on the specified operation.

    Args:
        operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Result of the calculation

    Raises:
        ValueError: If operation is not recognized or if division by zero
    """
    operations = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: {operation}. Valid operations are: {', '.join(operations.keys())}")

    return operations[operation](a, b)
