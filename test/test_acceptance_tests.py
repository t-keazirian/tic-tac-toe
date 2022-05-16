import io
import sys
import unittest
from unittest.mock import patch
from src.game import Game
from src.spanish_message import SpanishMessage
from test.mocks.mock_message import MockMessage


class TestAcceptance(unittest.TestCase):
    def game_playthrough(self):
        captured_output = io.StringIO()
        game = Game(message=MockMessage())
        sys.stdout = captured_output
        game.run()
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()

    @patch(
        "builtins.input",
        side_effect=["1", "1", "1", "1", "2", "3", "4", "5", "6", "7", "n"],
    )
    def test_player_X_wins_the_game(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input", side_effect=["1", "1", "1", "1", "2", "3", "5", "4", "8", "n"]
    )
    def test_player_O_wins_the_game(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "O")

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input",
        side_effect=["1", "1", "1", "1", "3", "2", "4", "5", "9", "6", "8", "7", "n"],
    )
    def test_play_through_ends_in_draw(self, mock_input):
        expected_message = MockMessage.game_over_message(self)

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input",
        side_effect=[
            "1",
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

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input",
        side_effect=["1", "1", "2", "1", "2", "1", "2", "3", "4", "5", "6", "7", "n"],
    )
    def test_player_one_wins_when_using_emojis(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "😃")

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input",
        side_effect=[
            "1",
            "1",
            "1",
            "1",
            "1",
            "2",
            "3",
            "4",
            "6",
            "7",
            "5",
            "8",
            "9",
            "n",
        ],
    )
    def test_play_through_and_X_wins_when_board_is_full(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input",
        side_effect=[
            "1",
            "blah",
            "1",
            "blah",
            "2",
            "blah",
            "1",
            "2",
            "1",
            "blah",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "blah",
            "n",
        ],
    )
    def test_invalid_inputs(self, mock_input):
        game_output = self.game_playthrough()

        self.assertIn(MockMessage.invalid_board_input(self), game_output)
        self.assertIn(MockMessage.invalid_menu_input(self), game_output)
        self.assertIn(MockMessage.invalid_repeat_game_input(self), game_output)
        self.assertIn(MockMessage.invalid_symbol_option(self), game_output)

    @patch(
        "builtins.input",
        side_effect=["2", "1", "1", "1", "2", "3", "4", "5", "6", "7", "n"],
    )
    def test_player_X_wins_the_game_in_spanish(self, mock_input):
        expected_message = SpanishMessage.declare_winner(self, "X")

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)

    @patch(
        "builtins.input",
        side_effect=["1", "3", "1", "2", "6", "8", "9", "n"],
    )
    def test_play_through_with_ai_unbeatable(self, mock_input):
        expected_message = MockMessage.declare_winner(self, "X")

        game_output = self.game_playthrough()

        self.assertIn(expected_message, game_output)
