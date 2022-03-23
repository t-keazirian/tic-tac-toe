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
        message.display_formatted_board(self)

    def get_prompt(self, total_marks_on_board):
        current_player = self.new_board.get_current_player(total_marks_on_board)
        if self.new_board.is_board_full(total_marks_on_board, self.board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def process_user_input(self):
        user_input_as_string = self.get_user_input()
        position_choice = self.convert_input_to_integer(user_input_as_string)
        self.new_board.take_turns_marking_board(
            position_choice, self.board, self.total_marks_on_board
        )
        self.total_marks_on_board = self.new_board.count_marks_in_board(
            self.board, self.player_one, self.player_two
        )
        return self.board

    def convert_input_to_integer(self, user_input):
        return int(user_input)

    def get_user_input(self):
        user_input = input()
        return user_input

    def progress_game(self):
        current_total_marks_on_board = self.new_board.count_marks_in_board(
            self.board, self.player_one, self.player_two
        )
        while current_total_marks_on_board != len(self.board):
            self.get_prompt(current_total_marks_on_board)
            self.process_user_input()
            current_total_marks_on_board = self.new_board.count_marks_in_board(
                self.board, self.player_one, self.player_two
            )

            self.get_formatted_board()
        else:
            self.get_prompt(current_total_marks_on_board)

    def run(self):
        message.display_welcome_message(self)
        self.get_formatted_board()
        self.progress_game()
