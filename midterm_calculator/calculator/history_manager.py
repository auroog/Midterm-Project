"""
History Manager module for managing calculator operation history.
"""
import pandas as pd

class HistoryManager:
    """
    Class to manage the history of calculator operations.
    """
    def __init__(self):
        self.history = pd.DataFrame(columns=['Operation', 'A', 'B', 'Result'])

    def add_to_history(self, operation, operand_a, operand_b, result):
        """Add a calculation result to history."""
        self.history = self.history.append({
            'Operation': operation,
            'A': operand_a,
            'B': operand_b,
            'Result': result
        }, ignore_index=True)

    def get_history(self):
        """Return the calculation history."""
        return self.history
