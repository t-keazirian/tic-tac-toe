from src.board import Board
from src.message import Message as message
from src.rules import Rules
from src.user_interface import UserInterface as user_interface


class Game:
    def __init__(self):
        self.board = Board()
        self.rules = Rules()
        self.game_board = self.board.starter_board
        self.player_one = self.board.player_one
        self.player_two = self.board.player_two
        self.total_marks_on_board = 0

    def get_formatted_board(self):
        message.display_formatted_board(self, self.game_board)

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def get_prompt(self, total_marks_on_board):
        current_player = self.get_current_player(total_marks_on_board)
        if self.board.determine_is_full(total_marks_on_board, self.game_board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def process_user_input(self):
        position_choice = user_interface.get_user_input(self)
        if self.board.determine_is_spot_taken(self.game_board, position_choice):
            message.display_spot_taken_message(self)
            self.process_user_input()
        self.board.mark_board(
            position_choice,
            self.game_board,
            self.get_current_player(self.total_marks_on_board),
        )
        self.total_marks_on_board = self.board.count_marks(self.game_board)
        return self.game_board

    def determine_winning_mark(self, total_marks_on_board):
        player = self.get_current_player(total_marks_on_board)
        if player == self.player_one:
            return self.player_two
        else:
            return self.player_one

    def play_game(self):
        total_marks_on_board = self.board.count_marks(self.game_board)
        while not self.board.determine_is_full(total_marks_on_board, self.game_board):
            self.get_prompt(total_marks_on_board)
            self.process_user_input()
            total_marks_on_board = self.board.count_marks(self.game_board)
            self.get_formatted_board()
            if self.rules.determine_is_winner(self.game_board):
                winner = self.determine_winning_mark(total_marks_on_board)
                message.display_winner_message(self, winner)
                break
            else:
                self.play_game()
                break
        else:
            self.get_prompt(total_marks_on_board)

    def run(self):
        message.display_welcome_message(self)
        self.get_formatted_board()
        self.play_game()
