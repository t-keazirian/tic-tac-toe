class SymbolOptions:
    def get_symbols(self, user_input):
        symbols = {
            "1": "😃",
            "2": "😡",
            "3": "😎",
            "4": "😜",
            "5": "😈",
            "6": "👻",
            "7": "👽",
            "8": "🤖",
            "9": "👾",
            "10": "🤡",
        }
        return symbols[user_input]
