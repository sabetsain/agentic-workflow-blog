"""
Calculator module providing basic arithmetic operations.

This module implements a simple calculator with support for addition,
subtraction, multiplication, and division operations.
"""

from .operations import add, subtract, multiply, divide


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
