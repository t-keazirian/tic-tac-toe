class Game:

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def get_welcome_message(self):
        return "Welcome to Tic Tac Toe"

    def initialize_board(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def run(self):
        print(self.get_welcome_message())
        print(self.initialize_board())
