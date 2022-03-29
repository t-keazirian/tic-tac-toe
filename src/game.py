from src.board import Board
from src.message import Message as message


class Game:
    def __init__(self):
        # initialize a new Board
        self.new_board = Board()
        self.board = self.new_board.starter_board
        self.player_one = self.new_board.player_one
        self.player_two = self.new_board.player_two
        self.total_marks_on_board = 0

    def get_formatted_board(self):
        message.display_formatted_board(self, self.board)

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def get_prompt(self, total_marks_on_board):
        current_player = self.get_current_player(total_marks_on_board)
        if self.new_board.is_full(total_marks_on_board, self.board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def get_prompt_for_occupied_spot(self, board, user_input):
        if self.new_board.is_spot_taken(board, user_input):
            message.display_spot_taken_message(self)

    def process_user_input(self):
        user_input_as_string = self.get_user_input()
        position_choice = self.convert_input_to_integer(user_input_as_string)
        # look at - not working - or should it go somewhere else?
        if self.new_board.is_spot_taken(self.board, position_choice):
            self.get_prompt_for_occupied_spot(self.board, position_choice)
        else:
            self.new_board.mark_board(
                position_choice, self.board, self.total_marks_on_board
            )
            self.total_marks_on_board = self.new_board.count_marks(
                self.board, self.player_one, self.player_two
            )
        # do I need this return?
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
