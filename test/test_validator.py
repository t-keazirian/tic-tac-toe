import unittest

from src.validator import Validator


class MockSymbol:
    def symbol_generator(self, user_input):
        symbols = {
            "1": "😃",
            "2": "😡",
            "3": "😎",
        }
        return symbols[user_input]


class TestValidator(unittest.TestCase):
    def test_is_integer_returns_true_when_input_is_integer(self):
        validator = Validator()
        test_move = "4"
        result = validator.is_integer(test_move)
        self.assertEqual(True, result)

    def test_is_integer_returns_true_when_input_is_not_integer(self):
        validator = Validator()
        test_move = "s"
        result = validator.is_integer(test_move)
        self.assertEqual(False, result)

    def test_if_correct_input_return_true(self):
        validator = Validator()
        test_spot = 8
        output = validator.is_in_range(test_spot)
        self.assertEqual(True, output)

    def test_if_incorrect_input_return_false(self):
        validator = Validator()
        test_spot = 10
        output = validator.is_in_range(test_spot)
        self.assertEqual(False, output)

    def test_if_NaN_inputted_return_false(self):
        validator = Validator()
        test_spot = "one"
        output = validator.is_in_range(test_spot)
        self.assertEqual(False, output)

    def test_spot_is_available_when_spot_is_not_taken(self):
        validator = Validator()
        test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_spot = 3
        result = validator.spot_is_available(test_board, test_spot)
        self.assertEqual(True, result)

    def test_spot_is_not_available_when_spot_is_taken(self):
        validator = Validator()
        test_board = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
        test_spot = 3
        result = validator.spot_is_available(test_board, test_spot)
        self.assertEqual(False, result)

    def test_move_is_not_valid_if_NaN(self):
        validator = Validator()
        test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_move = "one"
        result = validator.is_valid_move(test_board, test_move)
        self.assertEqual(False, result)

    def test_move_is_not_valid_if_an_integer_thats_out_of_range(self):
        validator = Validator()
        test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_move = "10"
        result = validator.is_valid_move(test_board, test_move)
        self.assertEqual(False, result)

    def test_move_is_not_valid_if_spot_is_not_available(self):
        validator = Validator()
        test_board = ["1", "2", "X", "4", "5", "6", "7", "8", "9"]
        test_move = "3"
        result = validator.is_valid_move(test_board, test_move)
        self.assertEqual(False, result)

    def test_move_is_valid_if_spot_is_available(self):
        validator = Validator()
        test_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        test_move = "5"
        self.assertTrue(validator.is_valid_move(test_board, test_move))

    def test_valid_play_again_input_returns_Y_if_valid_input_and_Y_inputted(
        self,
    ):
        validator = Validator()
        user_input = "y"
        self.assertEqual(True, validator.is_valid_play_again_input(user_input))

    def test_handle_play_again_input_returns_N_when_valid_input_and_N_inputted(
        self,
    ):
        validator = Validator()
        user_input = "n"
        self.assertEqual(True, validator.is_valid_play_again_input(user_input))

    def test_is_valid_play_again_input_returns_false_if_input_is_invalid(
        self,
    ):
        validator = Validator()
        user_input = "7"
        self.assertEqual(False, validator.is_valid_play_again_input(user_input))

    def test_is_valid_play_again_input_returns_false_if_number_is_inputted(
        self,
    ):
        validator = Validator()
        user_input = "s"
        self.assertEqual(False, validator.is_valid_play_again_input(user_input))

    def test_is_valid_play_again_input_returns_true_if_correct_input(
        self,
    ):
        validator = Validator()
        user_input = "y"
        self.assertEqual(True, validator.is_valid_play_again_input(user_input))

    def test_is_empty_string_returns_true_if_string_is_empty(self):
        validator = Validator()
        user_input = ""
        self.assertEqual(True, validator.is_empty_string(user_input))

    def test_is_empty_string_returns_false_if_string_is_not_empty(self):
        validator = Validator()
        user_input = "blah"
        self.assertEqual(False, validator.is_empty_string(user_input))

    def test_is_valid_symbol_returns_false_if_input_contains_numbers(self):
        validator = Validator()
        user_input = "1"
        self.assertEqual(False, validator.is_valid_symbol(user_input))

    def test_is_valid_symbol_returns_false_if_input_contains_empty_string(self):
        validator = Validator()
        user_input = ""
        self.assertEqual(False, validator.is_valid_symbol(user_input))

    def test_is_valid_symbol_returns_true_if_input_is_a_letter(self):
        validator = Validator()
        mockSymbol = MockSymbol()
        user_input = "1"
        symbol_choice = mockSymbol.symbol_generator(user_input)
        self.assertEqual(True, validator.is_valid_symbol(symbol_choice))
