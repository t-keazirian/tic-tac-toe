class UserInterface:
    def empty_line(self):
        print("")

    def display_message(self, message):
        self.empty_line()
        print(message)

    def display_board(self, board):
        self.empty_line()
        print(board)

    def get_user_input(self):
        user_input = input()
        self.empty_line()
        return user_input
