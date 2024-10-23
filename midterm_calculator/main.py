"""
Main module for the Python Calculator.
This module handles user input and executes commands/
"""

import logging
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.history_manager import HistoryManager

logging.basicConfig(level=logging.INFO)

def main():
    """Main function to run the calculator."""
    print("Welcome to the Python Calculator!")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'history' to see the calculation history.")
    print("Type 'exit' to quit.")

    history_manager = HistoryManager()

    while True:
        command = input("Enter command: ").lower()

        if command == 'exit':
            logging.info("Exiting the calculator.")
            break

        if command in ['add', 'subtract', 'multiply', 'divide']:
            try:
                operand_a = float(input("Enter first number: "))
                operand_b = float(input("Enter second number: "))

                if command == 'add':
                    result = AddCommand().execute(operand_a,operand_b)
                    histoy_manager.add_to_history('add', operand_a, operand_b, result)
                elif command == 'subtract':
                    result = SubtractCommand().execute(operand_a,operand_b)
                    histoy_manager.add_to_history('subtract', operand_a, operand_b, result)
                elif command == 'multiply':
                    result = MultiplyCommand().execute(operand_a,operand_b)
                    histoy_manager.add_to_history('multiply', operand_a, operand_b, result)
                elif command == 'divide':
                    result = DivideCommand().execute(operand_a,operand_b)
                    histoy_manager.add_to_history('divide', operand_a, operand_b, result)

                print("Result:", result)

            except ValueError:
                logging.error("Invalid input: Input must be numbers.")
                print("Invalid input. Please enter valid numbers.")
        elif command == 'history':
            print(history_manager.get_history())
        else:
            print("Unknown command. Type 'exit' to quit.")

if __name__ == "__main__":
    main()
