from src.board import Board
from src.message import Message
from src.rules import Rules
from src.user_interface import UserInterface
from src.validator import Validator
from src.symbol import SymbolOptions


class Game:
    def __init__(self, ui=UserInterface(), message=Message()):
        self.board = Board()
        self.rules = Rules()
        self.validator = Validator()
        self.symbol = SymbolOptions()
        self.ui = ui
        self.message = message
        self.game_board = self.board.starter_board
        self.player_one = "X"
        self.player_two = "O"
        self.total_marks_on_board = 0
        self.playing = True

    def should_change_symbols(self):
        self.ui.display_message(self.message.menu())
        user_input = self.ui.get_user_input()
        valid_user_input = self.validator.is_valid_menu_choice(user_input)
        while valid_user_input is False:
            self.ui.display_message(self.message.invalid_choose_symbol_input())
            user_input = self.ui.get_user_input()
            valid_user_input = self.validator.is_valid_menu_choice(user_input)
        if user_input == "1":
            self.ui.display_board(self.board.to_string(self.game_board))
            self.game_loop()
        if user_input == "2":
            self.ui.display_message(self.message.display_symbols())
            self.set_player_one_symbol()
            self.set_player_two_symbol()

    def set_player_one_symbol(self):
        self.ui.display_message(self.message.choose_symbol_player_one())
        symbol = self.ui.get_user_input()
        valid_symbol = self.validator.is_valid_symbol_choice_input(symbol)
        while not valid_symbol:
            self.ui.display_message(self.message.invalid_choose_symbol_input())
            symbol = self.ui.get_user_input()
            valid_symbol = self.validator.is_valid_symbol_choice_input(symbol)
        self.player_one = self.symbol.get_symbols(symbol)
        return self.player_one

    def set_player_two_symbol(self):
        self.ui.display_message(self.message.choose_symbol_player_two())
        symbol = self.ui.get_user_input()
        valid_symbol = self.validator.is_valid_symbol_choice_input(symbol)
        while not valid_symbol:
            self.ui.display_message(self.message.invalid_choose_symbol_input())
            symbol = self.ui.get_user_input()
            valid_symbol = self.validator.is_valid_symbol_choice_input(symbol)
        self.player_two = self.symbol.get_symbols(symbol)
        return self.player_two

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
        self.player_one = "X"
        self.player_two = "O"

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

    def handle_full_board(self):
        if self.rules.is_winner(self.game_board):
            self.handle_winning_game()
        else:
            self.handle_draw()

    def take_turns(self):
        self.prompt_for_move(self.total_marks_on_board)
        self.handle_mark_board()
        self.total_marks_on_board = self.board.count_marks(
            self.game_board, self.player_one, self.player_two
        )
        self.get_formatted_board()

    def ask_to_play_again(self):
        self.ui.display_message(self.message.play_again_prompt())
        answer = self.ui.get_user_input()
        while not self.validator.is_valid_play_again_input(answer):
            self.ui.display_message(self.message.invalid_repeat_game_input())
            answer = self.ui.get_user_input()
        if answer.upper() == "Y":
            self.new_game()
            self.should_change_symbols()
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
                self.handle_full_board()
                self.ask_to_play_again()
            else:
                self.take_turns()

    def run(self):
        self.ui.display_message(self.message.welcome_message())
        self.ui.display_message(self.message.rules())
        self.should_change_symbols()
        self.ui.display_board(self.board.to_string(self.game_board))
        self.game_loop()
        self.ui.display_message(self.message.goodbye_message())
