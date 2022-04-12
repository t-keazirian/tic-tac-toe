import unittest

from src.validation import Validation


class TestValidation(unittest.TestCase):
    def test_is_integer_returns_true_when_input_is_integer(self):
        validation = Validation()
        user_input = "4"
        result = validation.is_integer(user_input)
        self.assertEqual(True, result)

    def test_is_integer_returns_true_when_input_is_not_integer(self):
        validation = Validation()
        user_input = "s"
        result = validation.is_integer(user_input)
        self.assertEqual(False, result)

    def test_if_correct_input_return_true(self):
        validation = Validation()
        user_input = 8
        output = validation.input_in_range(user_input)
        self.assertEqual(True, output)

    def test_if_incorrect_input_return_false(self):
        validation = Validation()
        user_input = 10
        output = validation.input_in_range(user_input)
        self.assertEqual(False, output)

    def test_if_NaN_inputted_return_false(self):
        validation = Validation()
        user_input = "one"
        output = validation.input_in_range(user_input)
        self.assertEqual(False, output)

    def test_valid_play_again_input_returns_Y_if_valid_input_and_Y_inputted(
        self,
    ):
        validation = Validation()
        user_input = "y"
        self.assertEqual(True, validation.is_valid_play_again_input(user_input))

    def test_handle_play_again_input_returns_N_when_valid_input_and_N_inputted(
        self,
    ):
        validation = Validation()
        user_input = "n"
        self.assertEqual(True, validation.is_valid_play_again_input(user_input))

    def test_is_valid_play_again_input_returns_false_if_input_is_invalid(
        self,
    ):
        validation = Validation()
        user_input = "7"
        self.assertEqual(False, validation.is_valid_play_again_input(user_input))

    def test_is_valid_play_again_input_returns_false_if_number_is_inputted(
        self,
    ):
        validation = Validation()
        user_input = "s"
        self.assertEqual(False, validation.is_valid_play_again_input(user_input))

    def test_is_valid_play_again_input_returns_true_if_correct_input(
        self,
    ):
        validation = Validation()
        user_input = "y"
        self.assertEqual(True, validation.is_valid_play_again_input(user_input))

    def test_is_spot_taken_returns_true_when_spot_is_marked(self):
        validation = Validation()
        current_board = ["X", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 1
        player_one = "X"
        player_two = "O"
        spot_is_taken = validation.is_spot_taken(
            current_board, user_input, player_one, player_two
        )
        self.assertEqual(True, spot_is_taken)

    def test_is_spot_taken_returns_true_when_spot_is_marked_2(self):
        validation = Validation()
        current_board = ["1", "X", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        player_one = "X"
        player_two = "O"
        spot_is_taken = validation.is_spot_taken(
            current_board, user_input, player_one, player_two
        )
        self.assertEqual(True, spot_is_taken)

    def test_is_spot_taken_returns_false_with_multiple_spots_taken(self):
        validation = Validation()
        current_board = ["1", "X", "3", "O", "X", "6", "O", "8", "9"]
        user_input = 1
        player_one = "X"
        player_two = "O"
        spot_is_taken = validation.is_spot_taken(
            current_board, user_input, player_one, player_two
        )
        self.assertEqual(False, spot_is_taken)

    def test_is_spot_taken_returns_false_if_spot_is_avail(self):
        validation = Validation()
        current_board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        user_input = 2
        player_one = "X"
        player_two = "O"
        spot_is_taken = validation.is_spot_taken(
            current_board, user_input, player_one, player_two
        )
        self.assertEqual(False, spot_is_taken)

    def test_if_different_spot_is_taken_return_false(self):
        validation = Validation()
        current_board = ["1", "2", "3", "4", "5", "X", "7", "8", "9"]
        user_input = 4
        player_one = "X"
        player_two = "O"
        spot_is_taken = validation.is_spot_taken(
            current_board, user_input, player_one, player_two
        )
        self.assertEqual(False, spot_is_taken)

    def test_is_spot_taken_returns_false_with_multiple_spots_taken_2(self):
        validation = Validation()
        current_board = ["O", "X", "X", "O", "5", "6", "7", "8", "9"]
        user_input = 6
        player_one = "X"
        player_two = "O"
        spot_is_taken = validation.is_spot_taken(
            current_board, user_input, player_one, player_two
        )
        self.assertEqual(False, spot_is_taken)
