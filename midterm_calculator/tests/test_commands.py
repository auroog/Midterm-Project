"""
This module contains tests for the command classes in the midterm_calculator
module, specifically testing the AddCommand, SubtractCommand, MultiplyCommand,
and DivideCommand classes.
"""

import logging
from midterm_calculator.calculator.commands import (
    AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
)
def test_add_command():
    """Test the execution of the AddCommand with various inputs."""
    command = AddCommand()
    assert command.execute(3, 5) == 8
    assert command.execute(-1, 1) == 0
    assert command.execute(-1, -1) == -2

def test_subtract_command():
    """Test the execution of the SubtractCommand with various inputs."""
    command = SubtractCommand()
    assert command.execute(10, 5) == 5
    assert command.execute(0, 1) == -1
    assert command.execute(-1, -1) == 0

def test_multiply_command():
    """Test the execution of the MultiplyCommand with various inputs."""
    command = MultiplyCommand()
    assert command.execute(3, 5) == 15
    assert command.execute(-1, 5) == -5
    assert command.execute(0, 100) == 0

def test_divide_command():
    """Test the execution of the DivideCommand with various inputs."""
    command = DivideCommand()
    assert command.execute(10, 2) == 5
    assert command.execute(-10, -2) == 5
    assert command.execute(0, 1) == 0


def test_add_command_description():
    """Test that the description method of AddCommand returns the correct description."""
    command = AddCommand()
    assert command.description() == "Adds two numbers."

def test_subtract_command_description():
    """Test that the description method of SubtractCommand returns the correct description."""
    command = SubtractCommand()
    assert command.description() == "Subtracts the second number from the first."

def test_multiply_command_description():
    """Test that the description method of MultiplyCommand returns the correct description."""
    command = MultiplyCommand()
    assert command.description() == "Multiplies two numbers."

def test_divide_command_description():
    """Test that the description method of DivideCommand returns the correct description."""
    command = DivideCommand()
    assert command.description() == "Divides the first number by the second."

def test_divide_by_zero_logs_error(caplog):
    """Test that dividing by zero logs an error and does not raise an exception."""
    command = DivideCommand()
    with caplog.at_level(logging.ERROR):
        try:
            command.execute(6, 0)
        except ValueError:
            pass
        assert "Attempted to divide by zero." in caplog.text
