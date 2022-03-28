from src.board import Board
from src.message import Message as message
from src.player import Player


class Game:
    def __init__(self):
        # initialize a new Board
        self.new_board = Board()
        self.new_player = Player()
        self.board = self.new_board.starter_board
        self.player_one = self.new_board.player_one
        self.player_two = self.new_board.player_two
        self.total_marks_on_board = 0

    def get_formatted_board(self):
        message.display_formatted_board(self, self.board)

    def get_prompt(self, total_marks_on_board):
        current_player = self.new_player.get_current_player(total_marks_on_board)
        if self.new_board.is_full(total_marks_on_board, self.board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def process_user_input(self):
        user_input_as_string = self.get_user_input()
        position_choice = self.convert_input_to_integer(user_input_as_string)
        self.new_board.mark_board(
            position_choice, self.board, self.total_marks_on_board
        )
        self.total_marks_on_board = self.new_board.count_marks(
            self.board, self.player_one, self.player_two
        )
        return self.board

    def convert_input_to_integer(self, user_input):
        return int(user_input)

    def get_user_input(self):
        user_input = input()
        return user_input

    def play_game(self):
        total_marks_on_board = self.new_board.count_marks(
            self.board, self.player_one, self.player_two
        )
        while not self.new_board.is_full(total_marks_on_board, self.board):
            self.get_prompt(total_marks_on_board)
            self.process_user_input()
            total_marks_on_board = self.new_board.count_marks(
                self.board, self.player_one, self.player_two
            )

            self.get_formatted_board()
        else:
            self.get_prompt(total_marks_on_board)

    def run(self):
        message.display_welcome_message(self)
        self.get_formatted_board()
        self.play_game()
