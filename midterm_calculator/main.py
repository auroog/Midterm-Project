from calculator.operations import add, subtract, multiply, divide

def repl():
    print("Welcome to the Python Calculator!")
    print("Enter commands in the format: operation operand1 operand2")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit")

    while True:
        user_input = input(">>> ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        try:
            command, operand1, operand2 = user_input.split()
            operand1 = float(operand1)
            operand2 = float(operand2)

            if command == "add":
                result = add(operand1, operand2)
            elif command == "subtract":
                result = subtract(operand1, operand2)
            elif command == "multiply":
                result = multiply(operand1, operand2)
            elif command == "divide":
                result = divide(operand1, operand2)
            else:
                print("Unknown command. Please use 'add', 'subtract', 'multiply', or 'divide'.")
                continue

            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    repl()
