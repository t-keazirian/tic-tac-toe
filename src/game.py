from src.board import Board
from src.message import Message
from src.rules import Rules
from src.user_interface import UserInterface
from src.validation import Validation
from src.validator import Validator


class Game:
    def __init__(self, ui=UserInterface(), message=Message()):
        self.board = Board()
        self.rules = Rules()
        self.validation = Validation()
        self.validator = Validator()
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

    def prompt_for_full_board(self):
        self.ui.display_message(self.message.game_over_message())

    def get_prompt(self, total_marks_on_board):
        current_player = self.get_current_player(total_marks_on_board)
        if self.board.is_full(total_marks_on_board, self.game_board):
            self.ui.display_message(self.message.game_over_message())
        else:
            self.ui.display_message(self.message.prompt_for_move(current_player))

    def handle_mark_board(self):
        move = self.ui.get_user_input()
        valid_move = self.validator.is_valid_move(self.game_board, move)
        if not valid_move:
            self.ui.display_message(self.message.incorrect_board_input())
            move = self.ui.get_user_input()
            valid_move = self.validator.is_valid_move(self.game_board, move)
        else:
            self.board.mark_board(
                move,
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

    def handle_draw(self):
        self.ui.display_message(self.message.game_over_message())
        self.repeat_game()

    def handle_full_board(self):
        if self.rules.is_winner(self.game_board):
            self.handle_winning_game()
        else:
            self.handle_draw()

    def take_turns(self):
        self.get_prompt(self.total_marks_on_board)
        self.handle_mark_board()
        self.total_marks_on_board = self.board.count_marks(self.game_board)
        self.get_formatted_board()

    def play_again_prompt(self):
        self.ui.display_message(self.message.play_again_prompt())
        return self.ui.get_user_input()

    def repeat_game(self):
        self.ui.display_message(self.message.play_again_prompt())
        answer = self.ui.get_user_input()
        while not self.validator.is_valid_play_again_input(answer):
            self.ui.display_message(self.message.incorrect_repeat_game_input())
            answer = self.play_again_prompt()
        if answer.upper() == "Y":
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
