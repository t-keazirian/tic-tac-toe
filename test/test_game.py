import unittest
from unittest.mock import patch
from src.computer_player import ComputerPlayer

from src.game import Game
from src.human_player import HumanPlayer
from src.symbol import SymbolOptions
from test.mocks.mock_message import MockMessage
from src.board import Board
from src.ai_random import AIRandom


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(message=MockMessage())
        self.message = MockMessage()
        self.board = Board()
        self.ai_random = AIRandom()
        self.test_player_x = HumanPlayer("X", "message")
        self.test_player_o = HumanPlayer("O", "message")
        self.test_comp_player = ComputerPlayer("O", self.ai_random)

    @patch("builtins.print")
    def test_prompt_x_for_first_turn(self, mock_print):
        total_marks_on_board = 0

        self.game.prompt_for_move(total_marks_on_board)

        mock_print.assert_called_with(self.message.prompt_for_move(self.test_player_x))

    @patch("builtins.print")
    def test_prompt_o_for_second_turn(self, mock_print):
        total_marks_on_board = 1

        self.game.prompt_for_move(total_marks_on_board)

        mock_print.assert_called_with(self.message.prompt_for_move(self.test_player_o))

    @patch("builtins.print")
    def test_prompt_x_for_third_turn(self, mock_print):
        total_marks_on_board = 2

        self.game.prompt_for_move(total_marks_on_board)

        mock_print.assert_called_with(self.message.prompt_for_move(self.test_player_x))

    @patch("builtins.print")
    def test_handle_draw_displays_game_over_message(self, mock_print):
        self.game.handle_draw()

        mock_print.assert_called_with(self.message.game_over_message())

    def test_zero_turns_player_x_goes_first(self):
        total_marks_on_board = 0
        current_player = self.game.get_current_player(total_marks_on_board)

        self.assertEqual("X", current_player.mark)

    def test_one_turn_player_o_goes_next(self):
        total_marks_on_board = 1
        current_player = self.game.get_current_player(total_marks_on_board)

        self.assertEqual("O", current_player.mark)

    def test_two_turn_player_x_goes_next(self):
        total_marks_on_board = 2
        current_player = self.game.get_current_player(total_marks_on_board)

        self.assertEqual("X", current_player.mark)

    @patch("builtins.input", side_effect=["3"])
    def test_set_player_one_symbol_returns_symbol_with_input_3(self, mock_input):
        expected_symbol = SymbolOptions().get_symbol("3")

        test_message = self.message.choose_symbol_player_one()

        result = self.game.set_player_symbol(test_message)

        self.assertEqual(expected_symbol, result)

    @patch("builtins.input", side_effect=["2"])
    def test_set_player_two_symbol_returns_symbol_with_input_2(self, mock_input):
        expected_symbol = SymbolOptions().get_symbol("2")

        test_message = self.message.choose_symbol_player_two()

        result = self.game.set_player_symbol(test_message)

        self.assertEqual(expected_symbol, result)

    @patch("builtins.input", side_effect=["4"])
    def test_set_player_two_symbol_returns_symbol_with_input_4(self, mock_input):
        expected_symbol = SymbolOptions().get_symbol("4")

        test_message = self.message.choose_symbol_player_two()

        result = self.game.set_player_symbol(test_message)

        self.assertEqual(expected_symbol, result)

    def test_board_is_marked_by_computer_player(self):
        game_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]

        self.game.handle_mark_board(self.test_comp_player, game_board)

        marks_on_board = self.board.count_marks(game_board, "X", "O")

        self.assertEqual(2, marks_on_board)
