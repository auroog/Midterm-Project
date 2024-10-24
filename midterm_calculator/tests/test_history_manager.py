"""
Tests for the HistoryManager class in the calculator module.
"""

from midterm_calculator.calculator.history_manager import HistoryManager

def test_add_to_history():
    """Test adding an entry to the history."""
    manager = HistoryManager()
    manager.add_to_history("add", 2, 3, 5)

    history = manager.get_history()
    assert len(history) == 1
    assert history.iloc[0]['Operation'] == "add"
    assert history.iloc[0]['A'] == 2
    assert history.iloc[0]['B'] == 3
    assert history.iloc[0]['Result'] == 5

def test_get_history_empty():
    """Test getting history when it's empty."""
    manager = HistoryManager()
    history = manager.get_history()
    assert history.empty
