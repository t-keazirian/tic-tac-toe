from src.board import Board


class Message:
    def __init__(self):
        self.new_board = Board()

    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def display_game_over_message(self):
        print("Game Over!")

    def display_prompt_message_for_move(self, current_player):
        print(f"Player {current_player} - enter a number to place your mark")

    def display_error_prompt_for_occupied_spot(self):
        print("Spot is taken - choose another spot")

    def display_formatted_board(self):
        print(
            f"{self.new_board.starter_board[0]} | {self.new_board.starter_board[1]} | {self.new_board.starter_board[2]}\n--+--+--\n{self.new_board.starter_board[3]} | {self.new_board.starter_board[4]} | {self.new_board.starter_board[5]}\n--+--+--\n{self.new_board.starter_board[6]} | {self.new_board.starter_board[7]} | {self.new_board.starter_board[8]}"
        )
