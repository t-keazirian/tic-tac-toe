from src.board import Board
from src.message import Message
from src.rules import Rules
from src.spanish_message import SpanishMessage
from src.user_interface import UserInterface
from src.validator import Validator
from src.symbol import SymbolOptions
from src.config import config


class Game:
    def __init__(self, ui=UserInterface(), message=Message()):
        self.board = Board()
        self.rules = Rules()
        self.validator = Validator()
        self.symbol = SymbolOptions()
        self.ui = ui
        self.set_language(message)
        self.game_board = self.board.starter_board
        self.player_one = config["player_one"]
        self.player_two = config["player_two"]
        self.total_marks_on_board = 0
        self.playing = True

    def set_language(self, message):
        self.message = message

    def get_menu_choice(self, user_input, message):
        valid_user_input = self.validator.is_valid_menu_choice(user_input)
        if not valid_user_input:
            self.ui.display_message(message)
            new_user_input = self.ui.get_user_input()
            return self.get_menu_choice(new_user_input, message)
        return user_input

    def change_language(self):
        self.ui.display_message(self.message.choose_language())
        user_input = self.get_menu_choice(
            self.ui.get_user_input(), self.message.invalid_menu_input()
        )
        if user_input == config["play_in_spanish"]:
            self.set_language(SpanishMessage())

    def change_symbols(self):
        self.ui.display_message(self.message.menu())
        user_input = self.get_menu_choice(
            self.ui.get_user_input(), self.message.invalid_menu_input()
        )
        if user_input == config["play_with_symbols"]:
            self.ui.display_message(self.message.display_symbols())
            self.player_one = self.set_player_symbol(
                self.message.choose_symbol_player_one()
            )
            self.player_two = self.set_player_symbol(
                self.message.choose_symbol_player_two()
            )

    def set_player_symbol(self, message):
        self.ui.display_message(message)
        symbol = self.ui.get_user_input()
        valid_symbol = self.validator.is_valid_symbol_choice_input(symbol)
        while not valid_symbol:
            self.ui.display_message(self.message.invalid_symbol_option())
            symbol = self.ui.get_user_input()
            valid_symbol = self.validator.is_valid_symbol_choice_input(symbol)
        return self.symbol.get_symbol(symbol)

    def get_formatted_board(self):
        self.ui.display_board(self.board.to_string(self.game_board))

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def prompt_for_move(self, total_marks_on_board):
        current_player = self.get_current_player(total_marks_on_board)
        self.ui.display_message(self.message.prompt_for_move(current_player))

    def handle_mark_board(self):
        move = self.ui.get_user_input()
        valid_move = self.validator.is_valid_move(self.game_board, move)
        while not valid_move:
            self.ui.display_message(self.message.invalid_board_input())
            move = self.ui.get_user_input()
            valid_move = self.validator.is_valid_move(self.game_board, move)
        self.game_board = self.board.mark_board(
            move,
            self.game_board,
            self.get_current_player(self.total_marks_on_board),
        )
        self.total_marks_on_board = self.board.count_marks(
            self.game_board, self.player_one, self.player_two
        )

    def new_game(self):
        self.total_marks_on_board = 0
        self.game_board = Board().starter_board
        self.player_one = config["player_one"]
        self.player_two = config["player_two"]

    def get_winning_mark(self, total_marks_on_board):
        player = self.get_current_player(total_marks_on_board)
        if player == self.player_one:
            return self.player_two
        else:
            return self.player_one

    def handle_winning_game(self):
        winner = self.get_winning_mark(self.total_marks_on_board)
        self.ui.display_message(self.message.declare_winner(winner))

    def handle_draw(self):
        self.ui.display_message(self.message.game_over_message())

    def take_turns(self):
        self.prompt_for_move(self.total_marks_on_board)
        self.handle_mark_board()
        self.total_marks_on_board = self.board.count_marks(
            self.game_board, self.player_one, self.player_two
        )
        self.get_formatted_board()

    def repeat_game(self):
        self.new_game()
        self.change_symbols()
        self.ui.display_board(self.board.to_string(self.game_board))

    def ask_to_play_again(self):
        self.ui.display_message(self.message.play_again_prompt())
        answer = self.ui.get_user_input()
        while not self.validator.is_valid_play_again_input(answer):
            self.ui.display_message(self.message.invalid_repeat_game_input())
            answer = self.ui.get_user_input()
        if answer.upper() == config["play_again"]:
            self.repeat_game()
        else:
            self.playing = False

    def game_loop(self):
        while self.playing:
            if self.rules.is_winner(self.game_board):
                self.handle_winning_game()
                self.ask_to_play_again()
            elif self.board.is_full(
                self.board.count_marks(
                    self.game_board, self.player_one, self.player_two
                ),
                self.game_board,
            ):
                self.handle_draw()
                self.ask_to_play_again()
            else:
                self.take_turns()

    def run(self):
        self.ui.display_message(self.message.welcome_message())
        self.change_language()
        self.ui.display_message(self.message.rules())
        self.change_symbols()
        self.ui.display_board(self.board.to_string(self.game_board))
        self.game_loop()
        self.ui.display_message(self.message.goodbye_message())
