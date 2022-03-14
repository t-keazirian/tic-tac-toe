class Game:
    def hello_world(self):
        return "Hello, world!"

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def display_board(self):
        print(
            f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"
        )

    def run(self):
        self.display_welcome_message()
        self.display_board()
