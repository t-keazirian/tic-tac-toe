class Game:
    def hello_world(self):
        return "Hello, world!"

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def display_board(self):
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        print(
            f"{board[0]} | {board[1]} | {board[2]}\n---+---+---\n{board[3]} {board[4]} | {board[5]}\n---+---+---\n{board[6]} | {board[7]} | {board[8]}"
        )


if __name__ == "__main__":
    game = Game()
    game.display_welcome_message()
