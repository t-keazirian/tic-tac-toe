import unittest

from src.game import Game


class TestGame(unittest.TestCase):
    def test_dummy_test(self):
        subject = Game().hello_world
        self.assertEqual(subject(), "Hello, world!")

    def test_welcome_message(self):
        subject = Game().hello_world
        self.assertEqual(subject(), "Hello, world!")

    def test_print_board(self):
        subject = Game().hello_world
        self.assertEqual(subject(), "Hello, world!")
