import unittest
from src.symbol import SymbolOptions


class TestSymbolOptions(unittest.TestCase):
    def test_get_symbols_returns_symbol_1_if_1_is_inputted(self):
        symbol = SymbolOptions()
        user_input = "1"
        self.assertEqual("😃", symbol.get_symbols(user_input))
