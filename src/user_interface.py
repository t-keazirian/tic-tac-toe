class UserInterface:
    def display_message(self, message):
        print(message)

    def display_board(self, board):
        print(board)

    def get_user_input(self):
        user_input = input()
        return user_input

    def get_play_again_user_input(self, message):
        play_again_input = input()
        is_valid_input = self.valid_play_again_input(play_again_input)
        if is_valid_input:
            if play_again_input.upper() == "Y":
                return "Y"
            else:
                return "N"
        else:
            return self.handle_invalid_play_again_input(play_again_input, message)

    def valid_play_again_input(self, user_input):
        if user_input.upper() == "Y" or user_input.upper() == "N":
            return True
        else:
            return False

    def handle_invalid_play_again_input(self, user_input, message):
        valid_input = self.valid_play_again_input(user_input)
        while valid_input is False:
            self.display_message(message)
            user_input = self.get_play_again_user_input(message)
            valid_input = self.valid_play_again_input(user_input)
            break
        return user_input
