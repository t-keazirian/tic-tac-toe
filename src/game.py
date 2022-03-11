class Game:
    def hello_world(self):
        return "Hello, world!"

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def display_board(self, board):
        print(
            f"{board[0]} | {board[1]} | {board[2]}\n--+--+--\n{board[3]} | {board[4]} | {board[5]}\n--+--+--\n{board[6]} | {board[7]} | {board[8]}"
        )
