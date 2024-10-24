"""
This module contains command classes for performing arithmetic operations.
"""

import logging

logger = logging.getLogger(__name__)

class Command:
    """Base class for arithmetic commands."""
    def execute(self, operand_a: float, operand_b: float) -> float:
        """Execute the command with given operands."""
        raise NotImplementedError("Subclasses must implement the execute method.")

    def description(self) -> str:
        """Return a description of the command."""
        raise NotImplementedError("Subclasses must implement the description method.")

class AddCommand(Command):
    """Command to add two operands."""
    def execute(self, operand_a: float, operand_b: float) -> float:
        logger.info("Adding %s and %s", operand_a, operand_b)
        return operand_a + operand_b

    def description(self) -> str:
        """Return a description of the add command."""
        return "Adds two numbers."

class SubtractCommand(Command):
    """Command to subtract the second operand from the first."""
    def execute(self, operand_a: float, operand_b: float) -> float:
        logger.info("Subtracting %s from %s", operand_b, operand_a)
        return operand_a - operand_b

    def description(self) -> str:
        """Return a description of the subtract command."""
        return "Subtracts the second number from the first."

class MultiplyCommand(Command):
    """Command to multiply two operands."""
    def execute(self, operand_a: float, operand_b: float) -> float:
        logger.info("Multiplying %s and %s", operand_a, operand_b)
        return operand_a * operand_b

    def description(self) -> str:
        """Return a description of the multiply command."""
        return "Multiplies two numbers."

class DivideCommand(Command):
    """Command to divide the first operand by the second."""
    def execute(self, operand_a: float, operand_b: float) -> float:
        if operand_b == 0:
            logger.error("Attempted to divide by zero.")
            return "Error: Cannot divide by zero."
        logger.info("Dividing %s by %s", operand_a, operand_b)
        return operand_a / operand_b

    def description(self) -> str:
        """Return a description of the divide command."""
        return "Divides the first number by the second."
