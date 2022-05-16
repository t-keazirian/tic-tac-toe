import unittest
from src.human_player import HumanPlayer

from src.message import Message
from src.symbol import SymbolOptions


class TestMessage(unittest.TestCase):
    def setUp(self):
        self.message = Message()

    def test_welcome_message_prints_to_console(self):
        expected_message = "Welcome to Tic Tac Toe"

        actual_message = self.message.welcome_message()

        self.assertEqual(expected_message, actual_message)

    def test_menu_returns_menu_for_symbol_options(self):
        expected_message = """
Choose one of the options below:
1. Play game with symbols 'X' and 'O'
2. Choose your own symbols
"""

        actual_message = self.message.menu()

        self.assertEqual(expected_message, actual_message)

    def test_display_symbols_displays_symbols_and_message(self):
        symbols = SymbolOptions().symbols
        expected_message = (
            f"Type a number to choose the associated symbol from this list: \n{symbols}"
        )
        actual_message = self.message.display_symbols()

        self.assertEqual(expected_message, actual_message)

    def test_invalid_menu_input_prints_message(self):
        expected_message = "That input is invalid. Please choose from the list above."

        actual_message = self.message.invalid_menu_input()

        self.assertEqual(expected_message, actual_message)

    def test_invalid_symbol_option_prints_message(self):
        expected_message = "That input is invalid. Please enter a number 1-10."

        actual_message = self.message.invalid_symbol_option()

        self.assertEqual(expected_message, actual_message)

    def test_choose_symbol_player_one_prints_message(self):
        expected_message = "Player One - please choose your mark:"

        actual_message = self.message.choose_symbol_player_one()

        self.assertEqual(expected_message, actual_message)

    def test_choose_symbol_player_two_prints_message(self):
        expected_message = "Player Two - please choose your mark:"

        actual_message = self.message.choose_symbol_player_two()

        self.assertEqual(expected_message, actual_message)

    def test_game_over_prints_to_console(self):
        expected_message = "Game over - it's a draw!"

        actual_message = self.message.game_over_message()

        self.assertEqual(expected_message, actual_message)

    def test_X_player_is_prompted_for_move_when_is_current_player(self):
        player = HumanPlayer("X", "message")
        expected_message = f"Player {player.mark} - enter a number to place your mark"

        actual_message = self.message.prompt_for_move(player)

        self.assertEqual(expected_message, actual_message)

    def test_declare_winner_with_correct_mark_as_winner(self):
        winner = "X"
        expected_message = f"Congrats Player {winner} - you are the winner!"

        actual_message = self.message.declare_winner(winner)

        self.assertEqual(expected_message, actual_message)

    def test_invalid_board_input(self):
        expected_message = "That input is incorrect. Please input a number 1-9 for a spot that is not occupied."

        actual_message = self.message.invalid_board_input()

        self.assertEqual(expected_message, actual_message)

    def test_play_again_prompt(self):
        expected_message = "Would you like to play again? (Y/N)"

        actual_message = self.message.play_again_prompt()

        self.assertEqual(expected_message, actual_message)

    def test_goodbye_message(self):
        expected_message = "Thanks for playing - goodbye!"

        actual_message = self.message.goodbye_message()

        self.assertEqual(expected_message, actual_message)

    def test_invalid_repeat_game_message(self):
        expected_message = "That input is incorrect. Please input Y to play again or N to exit the game."

        actual_message = self.message.invalid_repeat_game_input()

        self.assertEqual(expected_message, actual_message)

    def test_print_rules_prints_rules_to_console(self):
        expected_message = """
Play this game by taking turns marking the board.
You will start by choosing between using the default X and O symbols, or your own symbol instead.
When prompted, type a number between 1 and 9 and press enter.
If that spot is taken, the computer will prompt you for a different spot.
The first player who gets three of their marks in a row wins!
If the board is full and neither player has three in a row, it is a draw and the game is over.
At the end of every game, you will have the option to play again or to exit.
"""

        actual_message = self.message.rules()

        self.assertEqual(expected_message, actual_message)

    def test_choose_language_prints_to_console(self):
        expected_message = """
Choose your language:
1. English
2. Spanish
"""

        actual_message = self.message.choose_language()

        self.assertEqual(expected_message, actual_message)

    def test_choose_players_prints_to_console(self):
        expected_message = """
Please make a selection from the options:
1. Human vs Human (2 players)
2. Human vs Simple Computer (1 player)
3. Human vs Unbeatable Computer (1 player)
"""

        actual_message = self.message.choose_players()

        self.assertEqual(expected_message, actual_message)

    def test_computer_go_first_prints_to_console(self):
        expected_message = """🚨 Computer will go first! 🚨

Here are the rules:
"""

        actual_message = self.message.computer_go_first()

        self.assertEqual(expected_message, actual_message)

    def test_human_go_first_prints_to_console(self):
        expected_message = """🚨 You will go first! 🚨

Here are the rules:
"""

        actual_message = self.message.human_go_first()

        self.assertEqual(expected_message, actual_message)
