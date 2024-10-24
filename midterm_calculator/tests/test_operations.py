"""
Test module for calculator operations.
This module contains tests for the Add, Subtract, Multiply, and Divide commands.
"""

import pytest
from midterm_calculator.calculator.operations import add, subtract, multiply, divide
from midterm_calculator.calculator.commands import (
    AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
)

# Tests for basic arithmetic operations
def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, -1) == -2

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(0, 3) == 0

def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    with pytest.raises(ValueError):
        divide(6, 0)

# Tests for command classes
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
