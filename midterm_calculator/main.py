"""
Main module for the Python Calculator.
This module handles user input and executes commands/
"""

import logging
import os
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.history_manager import HistoryManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    """Main function to run the calculator."""
    logging.info("Calculator program started.")

    print("Welcome to the Python Calculator!")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'history' to see the calculation history.")
    print("Type 'exit' to quit.")

    history_manager = HistoryManager()

    enable_history = os.getenv('ENABLE_HISTORY', 'true').lower() == 'true' 

    while True:
        command = input("Enter command: ").lower()
        logging.info(f"User entered command: {command}")

        if command == 'exit':
            logging.info("Exiting the calculator.")
            break

        if command in ['add', 'subtract', 'multiply', 'divide']:
            try:
                operand_a = float(input("Enter first number: "))
                operand_b = float(input("Enter second number: "))
                logging.info(f"Operands received: {operand_a}, {operand_b}")

                if command == 'add':
                    result = AddCommand().execute(operand_a,operand_b)
                    logging.info(f"Addition result: {result}"
                elif command == 'subtract':
                    result = SubtractCommand().execute(operand_a,operand_b)
                    logging.info(f"Subtraction result: {result}"
                elif command == 'multiply':
                    result = MultiplyCommand().execute(operand_a,operand_b)
                    logging.info(f"Multiplication result: {result}"
                elif command == 'divide':
                    result = DivideCommand().execute(operand_a,operand_b)
                    logging.info(f"Division result: {result}"

                print("Result:", result)

                if enable_history:
                    logging.info("History logging is enabled.")
                    history_manager.add_to_history(command, operand_a, operand_b, result)

            except ValueError:
                logging.error("Invalid input: Input must be numbers.")
                print("Invalid input. Please enter valid numbers.")
        elif command == 'history':
            logging.info("Displaying calculation history.")
            print(history_manager.get_history())
        else:
            logging.warning(f"Unknown command: {command}")
            print("Unknown command. Type 'exit' to quit.")

if __name__ == "__main__":
    main()
