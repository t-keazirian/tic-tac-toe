import re


class Validation:
    def is_integer(self, user_input):
        if re.match(r"^[0-9]*$", user_input) is None:
            return False
        else:
            return True

    def input_in_range(self, user_input):
        if user_input in range(1, 10):
            return True
        else:
            return False

    def is_valid_input(self, user_input):
        if self.is_integer(user_input) and self.input_in_range(user_input):
            return True
        else:
            return False
