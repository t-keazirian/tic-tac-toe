import io
import sys
import unittest
from unittest.mock import patch
from src.game import Game
from test.mocks.mock_message import MockMessage


class TestAcceptance(unittest.TestCase):
    def capture_output(self):
        captured_output = io.StringIO()
        game = Game(message=MockMessage())
        sys.stdout = captured_output
        game.run()
        sys.stdout = sys.__stdout__
        return captured_output

    @patch(
        "builtins.input", side_effect=["1", "1", "1", "2", "3", "4", "5", "6", "7", "n"]
    )
    def test_player_X_wins_the_game(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch("builtins.input", side_effect=["1", "1", "1", "2", "3", "5", "4", "8", "n"])
    def test_player_O_wins_the_game(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "O")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "1", "1", "3", "2", "4", "5", "9", "6", "8", "7", "n"],
    )
    def test_play_through_ends_in_draw(self, mock_input):
        expected_message = MockMessage.game_over_message(self)

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=[
            "1",
            "1",
            "1",
            "3",
            "2",
            "4",
            "5",
            "9",
            "6",
            "8",
            "7",
            "y",
            "1",
            "1",
            "2",
            "3",
            "5",
            "4",
            "8",
            "n",
        ],
    )
    def test_play_again_and_ends_with_X_win(self, mock_input):
        expected_message = MockMessage.game_over_message(self)

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "2", "1", "2", "1", "2", "3", "4", "5", "6", "7", "n"],
    )
    def test_player_one_wins_when_using_emojis(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "😃")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "1", "1", "2", "3", "4", "5", "6", "12", "7", "n"],
    )
    def test_invalid_input_for_mark_board(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "1", "1", "2", "3", "4", "5", "6", "7", "h", "n"],
    )
    def test_invalid_input_for_play_again(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["h", "1", "1", "1", "2", "3", "4", "5", "6", "7", "h", "n"],
    )
    def test_invalid_input_for_menu(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "1", "1", "1", "2", "3", "4", "6", "7", "5", "8", "9", "n"],
    )
    def test_play_through_and_X_wins_when_board_is_full(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "2", "h", "1", "2", "1", "2", "3", "4", "5", "6", "7", "n"],
    )
    def test_invalid_symbol_input(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "😃")

        captured_output = self.capture_output()

        self.assertIn(expected_message, captured_output.getvalue())
