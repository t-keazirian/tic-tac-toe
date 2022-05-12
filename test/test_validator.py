import unittest

from src.validator import Validator


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_is_integer_returns_true_if_input_is_integer(self):
        test_move = "4"

        result = self.validator.is_integer(test_move)

        self.assertTrue(result)

    def test_is_integer_returns_false_if_input_is_not_integer(self):
        test_move = "s"

        result = self.validator.is_integer(test_move)

        self.assertFalse(result)

    def test_if_correct_input_return_true(self):
        test_spot = 8

        output = self.validator.is_in_range(test_spot)

        self.assertTrue(output)

    def test_if_incorrect_input_return_false(self):
        test_spot = 10

        output = self.validator.is_in_range(test_spot)

        self.assertFalse(output)

    def test_if_NaN_inputted_return_false(self):
        test_spot = "one"

        output = self.validator.is_in_range(test_spot)

        self.assertFalse(output)

    def test_spot_is_available_returns_true_if_spot_is_not_taken(self):
        test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_spot = 3

        result = self.validator.spot_is_available(test_board, test_spot)

        self.assertTrue(result)

    def test_spot_is_available_returns_false_if_spot_is_taken(self):
        test_board = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
        test_spot = 3

        result = self.validator.spot_is_available(test_board, test_spot)

        self.assertFalse(result)

    def test_is_valid_move_returns_false_if_move_is_invalid(self):
        test_clean_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_board_with_marks = ["1", "O", "X", "4", "5", "6", "7", "8", "9"]

        self.assertFalse(self.validator.is_valid_move(test_clean_board, "one"))
        self.assertFalse(self.validator.is_valid_move(test_clean_board, ""))
        self.assertFalse(self.validator.is_valid_move(test_clean_board, "10"))
        self.assertFalse(self.validator.is_valid_move(test_board_with_marks, "3"))

    def test_is_valid_move_returns_true_if_move_is_valid(self):
        test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        self.assertTrue(self.validator.is_valid_move(test_board, "5"))
        self.assertTrue(self.validator.is_valid_move(test_board, "1"))

    def test_is_valid_play_again_input_returns_true_if_valid_input(self):
        self.assertTrue(self.validator.is_valid_play_again_input("y"))
        self.assertTrue(self.validator.is_valid_play_again_input("N"))
        self.assertTrue(self.validator.is_valid_play_again_input("y"))
        self.assertTrue(self.validator.is_valid_play_again_input("n"))

    def test_is_valid_play_again_input_returns_false_if_input_is_invalid(self):
        self.assertFalse(self.validator.is_valid_play_again_input("7"))
        self.assertFalse(self.validator.is_valid_play_again_input("s"))
        self.assertFalse(self.validator.is_valid_play_again_input("y y"))

    def test_is_empty_string_returns_true_if_string_is_empty(self):
        self.assertTrue(self.validator.is_empty_string(""))

    def test_is_empty_string_returns_false_if_string_is_not_empty(self):
        self.assertFalse(self.validator.is_empty_string("blah"))

    def test_is_valid_menu_choice_returns_false_if_choice_is_invalid(self):
        self.assertFalse(self.validator.is_valid_menu_choice("blah"))
        self.assertFalse(self.validator.is_valid_menu_choice("3"))
        self.assertFalse(self.validator.is_valid_menu_choice(""))

    def test_is_valid_menu_choice_returns_true_if_choice_is_valid(self):
        self.assertTrue(self.validator.is_valid_menu_choice("2"))
        self.assertTrue(self.validator.is_valid_menu_choice("1"))

    def test_is_valid_symbol_choice_returns_false_if_choice_is_11(self):
        self.assertFalse(self.validator.is_valid_symbol_choice_input("11"))
        self.assertFalse(self.validator.is_valid_symbol_choice_input("blah"))
