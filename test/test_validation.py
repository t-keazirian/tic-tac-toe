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
