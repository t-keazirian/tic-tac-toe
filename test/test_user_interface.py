import unittest
from unittest.mock import patch

from src.user_interface import UserInterface


class TestUserInterface(unittest.TestCase):
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

    def test_try_returns_true_when_input_is_integer(self):
        user_interface = UserInterface()
        user_input = "4"
        result = user_interface.is_integer(user_input)
        self.assertEqual(True, result)

    def test_try_returns_false_when_input_is_not_integer(self):
        user_interface = UserInterface()
        user_input = "s"
        result = user_interface.is_integer(user_input)
        self.assertEqual(False, result)
