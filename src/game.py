import re

from src.board import Board
from src.message import Message
from src.rules import Rules
from src.user_interface import UserInterface
from src.validation import Validation


class Game:
    def __init__(self, ui=UserInterface(), message=Message()):
        self.board = Board()
        self.rules = Rules()
        self.validation = Validation()
        self.ui = ui
        self.message = message
        self.game_board = self.board.starter_board
        self.player_one = self.board.player_one
        self.player_two = self.board.player_two
        self.total_marks_on_board = 0
        self.playing = True

    def get_formatted_board(self):
        self.ui.display_board(self.board.to_string(self.game_board))

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def get_prompt(self, total_marks_on_board):
        current_player = self.get_current_player(total_marks_on_board)
        if self.board.is_full(total_marks_on_board, self.game_board):
            self.ui.display_message(self.message.game_over_message())
        else:
            self.ui.display_message(self.message.prompt_for_move(current_player))

    def process_user_input(self):
        position_choice = self.validation.validate_move()
        if self.board.determine_is_spot_taken(self.game_board, position_choice):
            self.ui.display_message(self.message.spot_taken_message())
            self.process_user_input()
        self.board.mark_board(
            position_choice,
            self.game_board,
            self.get_current_player(self.total_marks_on_board),
        )
        self.total_marks_on_board = self.board.count_marks(self.game_board)
        return self.game_board

    def new_game(self):
        self.total_marks_on_board = 0
        self.game_board = Board().starter_board
        self.get_formatted_board()

    def get_winning_mark(self, total_marks_on_board):
        player = self.get_current_player(total_marks_on_board)
        if player == self.player_one:
            return self.player_two
        else:
            return self.player_one

    def handle_winning_game(self):
        winner = self.get_winning_mark(self.total_marks_on_board)
        self.ui.display_message(self.message.declare_winner(winner))
        self.repeat_game()

    def handle_full_board(self):
        if self.rules.is_winner(self.game_board):
            self.handle_winning_game()
        else:
            self.get_prompt(self.total_marks_on_board)
            self.repeat_game()

    def take_turns(self):
        self.get_prompt(self.total_marks_on_board)
        self.process_user_input()
        self.total_marks_on_board = self.board.count_marks(self.game_board)
        self.get_formatted_board()

    def repeat_game(self):
        self.ui.display_message(self.message.play_again_prompt())
        if self.validation.valid_play_again_input() == "Y":
            self.new_game()
        else:
            self.playing = False

    def game_loop(self):
        while self.playing:
            if self.rules.is_winner(self.game_board):
                self.handle_winning_game()
            elif self.board.is_full(
                self.board.count_marks(self.game_board), self.game_board
            ):
                self.handle_full_board()
            else:
                self.take_turns()

    def run(self):
        self.ui.display_message(self.message.welcome_message())
        self.ui.display_message(self.message.rules())
        self.ui.display_board(self.board.to_string(self.game_board))
        self.game_loop()
        self.ui.display_message(self.message.goodbye_message())
