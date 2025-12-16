"""Division operation module."""


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
