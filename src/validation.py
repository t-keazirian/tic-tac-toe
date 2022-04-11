import re

from src.message import Message as message
from src.user_interface import UserInterface as ui


class Validation:
    def validate_move_for_range(self, user_input):
        if self.input_in_range(user_input):
            return user_input
        else:
            return self.handle_incorrect_input(user_input)

    def input_in_range(self, user_input):
        if user_input in range(1, 10):
            return True
        else:
            return False

    def is_integer(self, user_input):
        if re.match(r"^[0-9]*$", user_input) is None:
            return False
        else:
            return True

    def validate_move(self):
        user_input = ui.get_user_input(self)
        is_integer = self.is_integer(user_input)
        if is_integer:
            user_integer = int(user_input)
            return self.validate_move_for_range(user_integer)
        else:
            return self.handle_incorrect_input(user_input)

    def handle_incorrect_input(self, user_input):
        valid_move = self.input_in_range(user_input)
        if valid_move is False:
            ui.display_message(self, message.incorrect_board_input(self))
            user_input = self.validate_move()
            valid_move = self.input_in_range(user_input)
        return user_input
