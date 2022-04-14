class Message:
    def welcome_message(self):
        return "Welcome to Tic Tac Toe"

    def menu(self):
        return """
Choose one of the options below:
1. Play game with symbols 'X' and 'O'
2. Choose your own symbols
"""

    def display_symbols(self):
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
        return (
            f"Type a number to choose the associated symbol from this list: \n{symbols}"
        )

    def invalid_choose_symbol_input(self):
        return "That input is invalid. Please enter 1 or 2."

    def invalid_symbol_option(self):
        return "That input is invalid. Please enter a number 1-10."

    def choose_symbol_player_one(self):
        return "Player One - please choose your mark:"

    def choose_symbol_player_two(self):
        return "Player Two - please choose your mark:"

    def rules(self):
        rules = """
Play this game by taking turns marking the board.
You will start by choosing between using the default X and O symbols, or your own symbol instead.
When prompted, type a number between 1 and 9 and press enter.
If that spot is taken, the computer will prompt you for a different spot.
The first player who gets three of their marks in a row wins!
If the board is full and neither player has three in a row, it is a draw and the game is over.
At the end of every game, you will have the option to play again or to exit.
"""
        return rules

    def game_over_message(self):
        return "Game over - it's a draw!"

    def prompt_for_move(self, current_player):
        return f"Player {current_player} - enter a number to place your mark"

    def declare_winner(self, winner):
        return f"Congrats Player {winner} - you are the winner!"

    def invalid_board_input(self):
        return "That input is incorrect. Please input a number 1-9 for a spot that is not occupied."

    def play_again_prompt(self):
        return "Would you like to play again? (Y/N)"

    def goodbye_message(self):
        return "Thanks for playing - goodbye!"

    def invalid_repeat_game_input(self):
        return "That input is incorrect. Please input Y to play again or N to exit the game."
