import unittest
from unittest.mock import patch

from src.message import Message
from src.user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
    @patch("builtins.print")
    def test_display_message_prints_welcome_message_passed_in(self, mock_print):
        user_interface = UserInterface()
        message = Message()
        message = message.welcome_message()
        user_interface.display_message(message)
        mock_print.assert_called_with("Welcome to Tic Tac Toe")

    @patch("builtins.print")
    def test_display_message_prints_current_player_message(self, mock_print):
        user_interface = UserInterface()
        message = Message()
        current_player = "X"
        message = message.prompt_for_move(current_player)
        user_interface.display_message(message)
        mock_print.assert_called_with(
            f"Player {current_player} - enter a number to place your mark"
        )

    @patch("builtins.print")
    def test_display_message_prints_formatted_board(self, mock_print):
        user_interface = UserInterface()
        message = Message()
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        message = message.formatted_board(board)
        user_interface.display_message(message)
        mock_print.assert_called_with(
            f"{board[0]} | {board[1]} | {board[2]}\n--+--+--\n{board[3]} | {board[4]} | {board[5]}\n--+--+--\n{board[6]} | {board[7]} | {board[8]}"
        )

    def test_if_correct_input_return_true(self):
        user_interface = UserInterface()
        user_input = 8
        output = user_interface.input_in_range(user_input)
        self.assertEqual(True, output)

    def test_if_incorrect_input_return_false(self):
        user_interface = UserInterface()
        user_input = 10
        output = user_interface.input_in_range(user_input)
        self.assertEqual(False, output)

    def test_if_NaN_inputted_return_false(self):
        user_interface = UserInterface()
        user_input = "one"
        output = user_interface.input_in_range(user_input)
        self.assertEqual(False, output)

    @patch("builtins.input", side_effect=["3"])
    def test_gets_user_input(self, mock_input):
        user_interface = UserInterface()
        output = user_interface.get_user_input()
        self.assertEqual(output, 3)

    @patch("builtins.input", side_effect=["3"])
    def test_gets_user_input_returns_string(self, mock_input):
        user_interface = UserInterface()
        output = type(user_interface.get_user_input())
        self.assertEqual(output, int)

    @patch("builtins.input", side_effect=["5"])
    def test_gets_user_input_function_not_returning_false_positive(self, mock_input):
        user_interface = UserInterface()
        output = user_interface.get_user_input()
        self.assertNotEqual(output, "3")

    def test_is_integer_returns_true_when_input_is_integer(self):
        user_interface = UserInterface()
        user_input = "4"
        result = user_interface.is_integer(user_input)
        self.assertEqual(True, result)

    def test_is_integer_returns_true_when_input_is_not_integer(self):
        user_interface = UserInterface()
        user_input = "s"
        result = user_interface.is_integer(user_input)
        self.assertEqual(False, result)

    @patch("builtins.input", side_effect=["Y"])
    def test_get_play_again_user_input_returns_true_when_input_is_Y(self, mock_input):
        user_interface = UserInterface()
        output = user_interface.get_play_again_user_input()
        self.assertEqual("Y", output)

    @patch("builtins.input", side_effect=["N"])
    def test_get_play_again_user_input_returns_false_when_input_is_N(self, mock_input):
        user_interface = UserInterface()
        output = user_interface.get_play_again_user_input()
        self.assertEqual("N", output)

    def test_handle_invalid_play_again_input_returns_true_when_user_input_is_Y(
        self,
    ):
        user_interface = UserInterface()
        user_input = "y"
        self.assertEqual(True, user_interface.valid_play_again_input(user_input))

    def test_handle_invalid_play_again_input_returns_true_when_user_input_is_N(
        self,
    ):
        user_interface = UserInterface()
        user_input = "n"
        self.assertEqual(True, user_interface.valid_play_again_input(user_input))

    def test_handle_invalid_play_again_input_returns_false_when_user_inputs_number(
        self,
    ):
        user_interface = UserInterface()
        user_input = "7"
        self.assertEqual(False, user_interface.valid_play_again_input(user_input))

    def test_handle_invalid_play_again_input_returns_false_when_incorrect_letter(
        self,
    ):
        user_interface = UserInterface()
        user_input = "s"
        self.assertEqual(False, user_interface.valid_play_again_input(user_input))
