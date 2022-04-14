from src.validator import Validator
from src.user_interface import UserInterface


class SymbolOptions:
    def __init__(self):
        self.ui = UserInterface()
        self.validator = Validator()

    def get_symbols(self, user_input):
        #    if no symbol is chosen, go with defaults
        #    if symbol is chosen, then go with that symbol instead
        symbols = {
            1: "😃",
            2: "😡",
            3: "😎",
            4: "😜",
            5: "😈",
            6: "👻",
            7: "👽",
            8: "🤖",
            9: "👾",
            10: "🤡",
        }
        print(symbols)

