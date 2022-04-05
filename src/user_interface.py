import re

from src.message import Message as message


class UserInterface:
    def get_user_input(self):
        user_input = input()
        is_integer = self.determine_is_integer(user_input)
        if is_integer:
            user_integer = int(user_input)
            return self.validate_move(user_integer)
        else:
            return self.handle_incorrect_input(user_input)

    def validate_move(self, user_input):
        if self.input_in_range(user_input):
            return user_input
        else:
            return self.handle_incorrect_input(user_input)

    def input_in_range(self, user_input):
        if user_input in range(1, 10):
            return True
        else:
            return False

    def determine_is_integer(self, user_input):
        if re.match(r"^[0-9]*$", user_input) is None:
            return False
        else:
            return True

    def handle_incorrect_input(self, user_input):
        valid_move = self.input_in_range(user_input)
        while valid_move is False:
            message.display_incorrect_input_message(self)
            user_input = self.get_user_input()
            valid_move = self.input_in_range(user_input)
            break
        return user_input
