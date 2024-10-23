"""
Main module for the Python Calculator.
This module handles user input and executes commands.
"""

import logging
import os
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator.history_manager import HistoryManager

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
numeric_level = getattr(logging, log_level, logging.INFO)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler('calculator.log')
file_handler.setLevel(numeric_level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)


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
        logging.info("User entered command: %s", command)

        if command == 'exit':
            logging.info("Exiting the calculator.")
            break

        if command in ['add', 'subtract', 'multiply', 'divide']:
            try:
                operand_a = float(input("Enter first number: "))
                operand_b = float(input("Enter second number: "))
                logging.info("Operands received: %s, %s", operand_a, operand_b)

                if command == 'add':
                    result = AddCommand().execute(operand_a, operand_b)
                    logging.info("Addition result: %s", result)
                elif command == 'subtract':
                    result = SubtractCommand().execute(operand_a, operand_b)
                    logging.info("Subtraction result: %s", result)
                elif command == 'multiply':
                    result = MultiplyCommand().execute(operand_a, operand_b)
                    logging.info("Multiplication result: %s", result)
                elif command == 'divide':
                    result = DivideCommand().execute(operand_a, operand_b)
                    logging.info("Division result: %s", result)

                print("Result:", result)

                if enable_history:
                    history_manager.add_to_history(command, operand_a, operand_b, result)

            except ValueError as error:
                logging.error("Invalid input: %s", str(error))
                print("Invalid input. Please enter valid numbers.")
        elif command == 'history':
            logging.info("Displaying calculation history.")
            print(history_manager.get_history())
        else:
            logging.warning("Unknown command: %s", command)
            print("Unknown command. Type 'exit' to quit.")

if __name__ == "__main__":
    main()
