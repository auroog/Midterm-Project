import logging
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

logging.basicConfig(level=logging.INFO)

def main():
    """Main function to run the calculator."""
    print("Welcome to the Python Calculator!")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit.")

    while True:
        command = input("Enter command: ").lower()

        if command == 'exit':
            logging.info("Exiting the calculator.")
            break

        if command in ['add', 'subtract', 'multiply', 'divide']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if command == 'add':
                    result = AddCommand().execute(a, b)
                elif command == 'subtract':
                    result = SubtractCommand().execute(a, b)
                elif command == 'multiply':
                    result = MultiplyCommand().execute(a, b)
                elif command == 'divide':
                    result = DivideCommand().execute(a, b)

                print("Result:", result)

            except ValueError:
                logging.error("Invalid input: Input must be numbers.")
                print("Invalid input. Please enter valid numbers.")
        else:
            print("Unknown command. Type 'exit' to quit.")

if __name__ == "__main__":
    main()
