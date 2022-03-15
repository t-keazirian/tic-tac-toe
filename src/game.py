class Game:

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def get_welcome_message(self):
        return "Welcome to Tic Tac Toe"

    def initialize_board(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def handle_prompt_message(self):
        return "Choose a number 1-9 to input your player: "

    def handle_first_player(self):
        position_choice = input()
        position_choice = int(position_choice) - 1
        self.board[position_choice] = "X"
        print(self.initialize_board())

    def run(self):
        print(self.get_welcome_message())
        print(self.initialize_board())
        print(self.handle_prompt_message())
        self.handle_first_player()
