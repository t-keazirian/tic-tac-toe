from src.board import Board
from src.message import Message as message


class Game:
    def __init__(self):
        # initialize a new Board
        self.new_board = Board()
        self.board = self.new_board.starter_board
        self.player_one = "X"
        self.player_two = "O"
        self.total_marks_on_board = 0

    def get_formatted_board(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def get_prompt(self, total_marks_on_board):
        current_player = self.new_board.get_current_player(total_marks_on_board)
        if self.new_board.is_board_full(total_marks_on_board, self.board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def process_user_input(self):
        position_choice = int(input())
        self.new_board.place_mark_on_board(
            position_choice, self.board, self.total_marks_on_board
        )
        self.total_marks_on_board += 1

    def convert_input_to_integer(self, user_input):
        return int(user_input)

    def get_user_input(self):
        position_choice = input()
        return position_choice

    def progress_game(self):
        current_total_marks_on_board = self.new_board.count_marks_in_board(
            self.board, self.player_one, self.player_two
        )
        while current_total_marks_on_board != len(self.board):
            self.get_prompt(current_total_marks_on_board)
            self.process_user_input()
            current_total_marks_on_board += 1
            print(self.get_formatted_board())
        else:
            self.get_prompt(current_total_marks_on_board)

    def play_new_game(self):
        message.display_welcome_message(self)
        print(self.get_formatted_board())
        self.progress_game()
