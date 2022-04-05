from src.message import Message as message


class UserInterface:
    def get_user_input(self):
        user_input = input()
        user_integer = int(user_input)
        valid_move = self.determine_is_correct_input(user_integer)
        if valid_move:
            return user_integer
        else:
            user_input = self.handle_incorrect_input(user_integer)
            return user_input

    def determine_is_correct_input(self, user_input):
        if user_input in range(1, 10):
            return True
        else:
            return False

    def handle_incorrect_input(self, user_input):
        valid_move = self.determine_is_correct_input(user_input)
        while valid_move is False:
            message.display_incorrect_input_message(self)
            user_input = self.get_user_input()
            valid_move = self.determine_is_correct_input(user_input)
            break
        return user_input
