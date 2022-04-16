import unittest

from src.message import Message
from src.symbol import SymbolOptions


class TestMessage(unittest.TestCase):
    def test_welcome_message_prints_to_console(self):
        message = Message()
        expected_message = "Welcome to Tic Tac Toe"
        actual_message = message.welcome_message()
        self.assertEqual(expected_message, actual_message)

    def test_menu_returns_menu_for_symbol_options(self):
        message = Message()
        expected_message = """
Choose one of the options below:
1. Play game with symbols 'X' and 'O'
2. Choose your own symbols
"""

        actual_message = message.menu()
        self.assertEqual(expected_message, actual_message)

    def test_display_symbols_displays_symbols_and_message(self):
        message = Message()
        symbols = SymbolOptions().symbols

        expected_message = (
            f"Type a number to choose the associated symbol from this list: \n{symbols}"
        )
        actual_message = message.display_symbols()
        self.assertEqual(expected_message, actual_message)

    def test_invalid_choose_symbol_input_prints_message(self):
        message = Message()
        expected_message = "That input is invalid. Please enter 1 or 2."
        actual_message = message.invalid_choose_symbol_input()
        self.assertEqual(expected_message, actual_message)

    def test_invalid_symbol_option_prints_message(self):
        message = Message()
        expected_message = "That input is invalid. Please enter a number 1-10."
        actual_message = message.invalid_symbol_option()
        self.assertEqual(expected_message, actual_message)

    def test_choose_symbol_player_one_prints_message(self):
        message = Message()
        expected_message = "Player One - please choose your mark:"
        actual_message = message.choose_symbol_player_one()
        self.assertEqual(expected_message, actual_message)

    def test_choose_symbol_player_two_prints_message(self):
        message = Message()
        expected_message = "Player Two - please choose your mark:"
        actual_message = message.choose_symbol_player_two()
        self.assertEqual(expected_message, actual_message)

    def test_game_over_prints_to_console(self):
        message = Message()
        expected_message = "Game over - it's a draw!"
        actual_message = message.game_over_message()
        self.assertEqual(expected_message, actual_message)

    def test_X_player_is_prompted_for_move_when_is_current_player(self):
        message = Message()
        current_player = "X"
        expected_message = (
            f"Player {current_player} - enter a number to place your mark"
        )
        actual_message = message.prompt_for_move(current_player)
        self.assertEqual(expected_message, actual_message)

    def test_declare_winner_with_correct_mark_as_winner(self):
        message = Message()
        winner = "X"
        expected_message = f"Congrats Player {winner} - you are the winner!"
        actual_message = message.declare_winner(winner)
        self.assertEqual(expected_message, actual_message)

    def test_invalid_board_input(self):
        message = Message()
        expected_message = "That input is incorrect. Please input a number 1-9 for a spot that is not occupied."
        actual_message = message.invalid_board_input()
        self.assertEqual(expected_message, actual_message)

    def test_play_again_prompt(self):
        message = Message()
        expected_message = "Would you like to play again? (Y/N)"
        actual_message = message.play_again_prompt()
        self.assertEqual(expected_message, actual_message)

    def test_goodbye_message(self):
        message = Message()
        expected_message = "Thanks for playing - goodbye!"
        actual_message = message.goodbye_message()
        self.assertEqual(expected_message, actual_message)

    def test_invalid_repeat_game_message(self):
        message = Message()
        expected_message = "That input is incorrect. Please input Y to play again or N to exit the game."
        actual_message = message.invalid_repeat_game_input()
        self.assertEqual(expected_message, actual_message)

    def test_print_rules_prints_rules_to_console(self):
        message = Message()
        rules = """
Play this game by taking turns marking the board.
You will start by choosing between using the default X and O symbols, or your own symbol instead.
When prompted, type a number between 1 and 9 and press enter.
If that spot is taken, the computer will prompt you for a different spot.
The first player who gets three of their marks in a row wins!
If the board is full and neither player has three in a row, it is a draw and the game is over.
At the end of every game, you will have the option to play again or to exit.
"""
        actual_message = message.rules()
        self.assertEqual(rules, actual_message)
