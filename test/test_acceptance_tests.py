import io
import sys
import unittest
from unittest.mock import patch
from src.game import Game
from test.mocks.mock_message import MockMessage


class TestAcceptance(unittest.TestCase):
    @patch("builtins.input", side_effect=["1","1", "1", "2", "3", "4", "5", "6", "7", "n"])
    def test_player_X_wins_the_game(self, mock_input):
        capturedOuput = io.StringIO()
        game = Game(message=MockMessage())
        expected_message = MockMessage.declare_winner(self, "X")

        sys.stdout = capturedOuput
        game.run()
        sys.stdout = sys.__stdout__

        self.assertIn(expected_message, capturedOuput.getvalue())
