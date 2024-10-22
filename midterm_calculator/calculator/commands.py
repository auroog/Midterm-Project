class Command:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement the execute method")

class AddCommand(Command):
    def execute(self, a, b):
        return a + b

class SubtractCommand(Command):
    def execute(self, a, b):
        return a - b

class MultiplyCommand(Command):
    def execute(self, a, b):
        return a * b

class DivideCommand(Command):
    def execute(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
