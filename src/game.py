from src.board import Board
from src.message import Message as message
from src.rules import Rules
from src.user_interface import UserInterface


class Game:
    def __init__(self, ui=UserInterface()):
        self.board = Board()
        self.rules = Rules()
        self.user_interface = ui
        self.game_board = self.board.starter_board
        self.player_one = self.board.player_one
        self.player_two = self.board.player_two
        self.total_marks_on_board = 0
        self.play_again = False

    def get_formatted_board(self):
        message.display_formatted_board(self, self.game_board)

    def get_current_player(self, total_marks_on_board):
        if total_marks_on_board % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def get_prompt(self, total_marks_on_board):
        current_player = self.get_current_player(total_marks_on_board)
        if self.board.is_full(total_marks_on_board, self.game_board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def process_user_input(self):
        position_choice = self.user_interface.get_user_input()
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

    def new_game(self):
        self.total_marks_on_board = 0
        self.game_board = Board().starter_board
        self.get_formatted_board()
        self.play_game()

    def get_winning_mark(self, total_marks_on_board):
        player = self.get_current_player(total_marks_on_board)
        if player == self.player_one:
            return self.player_two
        else:
            return self.player_one

    def handle_winning_game(self, board):
        winner = self.get_winning_mark(self.total_marks_on_board)
        message.display_winner_message(self, winner)
        self.repeat_game()

    def handle_draw(self):
        self.get_prompt(self.total_marks_on_board)
        self.process_user_input()
        self.total_marks_on_board = self.board.count_marks(self.game_board)
        self.get_formatted_board()
        self.play_game()

    def repeat_game(self):
        message.display_play_again(self)
        self.play_again = False
        if self.user_interface.get_play_again_user_input() == "Y":
            self.play_again = True
        while self.play_again:
            self.new_game()
        else:
            self.play_again = False

    def play_game(self):
        total_marks_on_board = self.board.count_marks(self.game_board)
        while not self.board.is_full(total_marks_on_board, self.game_board):
            if self.rules.is_winner(self.game_board):
                self.handle_winning_game(self.game_board)
                break
            else:
                self.handle_draw()
                break
        else:
            self.get_prompt(total_marks_on_board)
            self.repeat_game()

    def run(self):
        message.display_welcome_message(self)
        self.new_game()
        message.display_goodbye_message(self)
