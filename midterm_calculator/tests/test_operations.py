"""
Test module for calculator operations.
This module contains tests for the Add, Subtract, Multiply, and Divide commands.
"""

from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def test_add_command():
    """Test the addition operation."""
    command = AddCommand()
    assert command.execute(2, 3) == 5

def test_subtract_command():
    """Test the subtraction operation."""
    command = SubtractCommand()
    assert command.execute(5, 3) == 2

def test_multiply_command():
    """Test the multiplication operation."""
    command = MultiplyCommand()
    assert command.execute(2, 3) == 6

def test_divide_command():
    """Test the division operation."""
    command = DivideCommand()
    assert command.execute(6, 3) == 2
    assert command.execute(6, 0) == "Error: Cannot divide by zero."
