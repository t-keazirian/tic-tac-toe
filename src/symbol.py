class SymbolOptions:
    def __init__(self):
        self.symbols = {
            "1": "😃",
            "2": "😡",
            "3": "😎",
            "4": "😜",
            "5": "😈",
            "6": "👻",
            "7": "👽",
            "8": "🤖",
            "9": "🙀",
            "10": "🤡",
        }

    def get_symbol(self, user_input):
        return self.symbols[user_input]
