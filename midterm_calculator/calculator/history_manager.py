"""
History Manager module for managing calculator operation history.
"""
import logging
import pandas as pd

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("calculator_history.log"),
        logging.StreamHandler()
    ]
)

class HistoryManager:
    """
    Class to manage the history of calculator operations.
    """
    def __init__(self):
        self.history = pd.DataFrame(columns=['Operation', 'A', 'B', 'Result'])

    def add_to_history(self, operation: str, operand_a: float,
                       operand_b: float, result: float) -> None:
        """Add a calculation result to history."""
        new_entry = pd.DataFrame({
            'Operation': [operation],
            'A': [operand_a],
            'B': [operand_b],
            'Result': [result]
        })
        self.history = pd.concat([self.history, new_entry], ignore_index=True)

        logging.info(
            'Added to history: %s(%s, %s) = %s',
            operation, operand_a, operand_b, result)

    def get_history(self) -> pd.DataFrame:
        """Return the calculation history."""
        return self.history

    def __repr__(self) -> str:
        """Return a string representation of the history manager."""
        return f"HistoryManager(history={self.history})"
