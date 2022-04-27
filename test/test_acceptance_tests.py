import io
import sys
import unittest
from unittest.mock import patch
from src.game import Game
from test.mocks.mock_message import MockMessage


class TestAcceptance(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "1", "2", "3", "4", "5", "6", "7", "n"])
    def test_player_X_wins_the_game(self, mock_input):
        capturedOuput = io.StringIO()
        game = Game(message=MockMessage())
        expected_message = MockMessage.declare_winner(self, "X")

        sys.stdout = capturedOuput
        game.run()
        sys.stdout = sys.__stdout__

        self.assertIn(expected_message, capturedOuput.getvalue())

    @patch("builtins.input", side_effect=["1", "1", "2", "3", "5", "4", "8", "n"])
    def test_player_O_wins_the_game(self, mock_input):
        capturedOuput = io.StringIO()
        game = Game(message=MockMessage())
        expected_message = MockMessage.declare_winner(self, "O")

        sys.stdout = capturedOuput
        game.run()
        sys.stdout = sys.__stdout__

        self.assertIn(expected_message, capturedOuput.getvalue())

    @patch(
        "builtins.input",
        side_effect=["1", "1", "3", "2", "4", "5", "9", "6", "8", "7", "n"],
    )
    def test_play_through_ends_in_draw(self, mock_input):
        capturedOuput = io.StringIO()
        game = Game(message=MockMessage())
        expected_message = MockMessage.game_over_message(self)

        sys.stdout = capturedOuput
        game.run()
        sys.stdout = sys.__stdout__

        self.assertIn(expected_message, capturedOuput.getvalue())

    @patch(
        "builtins.input",
        side_effect=[
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
        capturedOuput = io.StringIO()
        game = Game(message=MockMessage())
        expected_message = MockMessage.game_over_message(self)

        sys.stdout = capturedOuput
        game.run()
        sys.stdout = sys.__stdout__

        self.assertIn(expected_message, capturedOuput.getvalue())

    @patch(
        "builtins.input",
        side_effect=["2", "1", "2", "1", "2", "3", "4", "5", "6", "7", "n"],
    )
    def test_player_one_wins_when_using_emojis(self, mock_input):
        capturedOuput = io.StringIO()
        game = Game(message=MockMessage())
        expected_message = MockMessage.declare_winner(self, "😃")

        sys.stdout = capturedOuput
        game.run()
        sys.stdout = sys.__stdout__

        self.assertIn(expected_message, capturedOuput.getvalue())
