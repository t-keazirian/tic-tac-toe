import re

from src.message import Message as message
from src.user_interface import UserInterface as ui


class Validation:
    def validate_move_for_range(self, user_input):
        user_input = int(user_input)
        if self.input_in_range(user_input):
            return user_input
        else:
            return self.handle_invalid_board_placement_input(user_input)

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
            return self.validate_move_for_range(user_input)
        else:
            return self.handle_invalid_board_placement_input(user_input)

    def handle_invalid_board_placement_input(self, user_input):
        valid_move = self.input_in_range(user_input)
        if valid_move is False:
            ui.display_message(self, message.incorrect_board_input(self))
            user_input = self.validate_move()
            valid_move = self.input_in_range(user_input)
        return user_input

    def valid_play_again_input(self):
        user_input = ui.get_play_again_user_input(self)
        valid_input = self.is_valid_play_again_input(user_input)
        if valid_input:
            if user_input.upper() == "Y":
                return "Y"
            else:
                return "N"
        else:
            return self.handle_invalid_play_again_input(user_input)

    def is_valid_play_again_input(self, user_input):
        if user_input.upper() == "Y" or user_input.upper() == "N":
            return True
        else:
            return False

    def handle_invalid_play_again_input(self, user_input):
        valid_input = self.is_valid_play_again_input(user_input)
        if valid_input is False:
            ui.display_message(self, message.incorrect_repeat_game_input(self))
            user_input = self.valid_play_again_input()
            valid_input = self.is_valid_play_again_input(user_input)
        return user_input
