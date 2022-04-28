import unittest
from unittest.mock import patch

from src.game import Game
from src.symbol import SymbolOptions
from test.mocks.mock_message import MockMessage


class TestGame(unittest.TestCase):
    @patch("builtins.print")
    def test_prompt_x_for_first_turn(self, mock_print):
        message = MockMessage()
        game = Game(message=message)
        total_marks_on_board = 0
        game.prompt_for_move(total_marks_on_board)
        mock_print.assert_called_with(message.prompt_for_move("X"))

    @patch("builtins.print")
    def test_prompt_o_for_second_turn(self, mock_print):
        message = MockMessage()
        game = Game(message=message)
        total_marks_on_board = 1
        game.prompt_for_move(total_marks_on_board)
        mock_print.assert_called_with(message.prompt_for_move("O"))

    @patch("builtins.print")
    def test_prompt_x_for_third_turn(self, mock_print):
        message = MockMessage()
        game = Game(message=message)
        total_marks_on_board = 2
        game.prompt_for_move(total_marks_on_board)
        mock_print.assert_called_with(message.prompt_for_move("X"))

    @patch("builtins.print")
    def test_handle_draw_displays_game_over_message(self, mock_print):
        message = MockMessage()
        game = Game(message=message)
        game.handle_draw()
        mock_print.assert_called_with(message.game_over_message())

    def test_zero_turns_player_x_goes_first(self):
        game = Game()
        total_marks_on_board = 0
        current_player = game.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_one_turn_player_o_goes_next(self):
        game = Game()
        total_marks_on_board = 1
        current_player = game.get_current_player(total_marks_on_board)
        self.assertEqual("O", current_player)

    def test_two_turn_player_x_goes_next(self):
        game = Game()
        total_marks_on_board = 2
        current_player = game.get_current_player(total_marks_on_board)
        self.assertEqual("X", current_player)

    def test_if_current_player_is_O_then_X_wins(self):
        game = Game()
        total_marks_on_board = 5
        winner = game.get_winning_mark(total_marks_on_board)
        self.assertEqual("X", winner)

    def test_if_current_player_is_X_then_O_wins(self):
        game = Game()
        total_marks_on_board = 6
        winner = game.get_winning_mark(total_marks_on_board)
        self.assertEqual("O", winner)

    @patch("builtins.input", side_effect=["3"])
    def test_set_player_one_symbol_returns_symbol_with_input_3(self, mock_input):
        game = Game()
        message = MockMessage()

        expected_symbol = SymbolOptions().get_symbol("3")

        message = message.choose_symbol_player_one()

        result = game.set_player_symbol(message)

        self.assertEqual(expected_symbol, result)

    @patch("builtins.input", side_effect=["2"])
    def test_set_player_two_symbol_returns_symbol_with_input_2(self, mock_input):
        game = Game()
        message = MockMessage()

        expected_symbol = SymbolOptions().get_symbol("2")

        message = message.choose_symbol_player_two()

        result = game.set_player_symbol(message)

        self.assertEqual(expected_symbol, result)

    @patch("builtins.input", side_effect=["4"])
    def test_set_player_two_symbol_returns_symbol_with_input_4(self, mock_input):
        game = Game()
        message = MockMessage()

        expected_symbol = SymbolOptions().get_symbol("4")

        message = message.choose_symbol_player_two()

        result = game.set_player_symbol(message)

        self.assertEqual(expected_symbol, result)
