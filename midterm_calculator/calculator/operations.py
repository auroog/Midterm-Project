"""
Operations module for performing arithmetic operations in the calculator.
"""


def add(operand_a, operand_b):
    """
    Test the add function.

    This function tests the `add` operation with both positive and negative numbers.
    """
    return operand_a + operand_b

def subtract(operand_a, operand_b):
    """
    Test the subtract function.

    This function tests the `subtract` operation with both positive and negative numbers.
    """
    return operand_a - operand_b

def multiply(operand_a, operand_b):
    """
    Test the multiply function.

    This function tests the `multiply` operation with various numbers, including zero.
    """
    return operand_a * operand_b

def divide(operand_a, operand_b):
    """
    Test the divide function.

    This function tests the `divide` operation, including a check for division by zero.
    """
    if operand_b == 0:
        raise ValueError("Cannot divide by zero")
    return operand_a / operand_b
