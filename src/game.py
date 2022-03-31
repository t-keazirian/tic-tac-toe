from src.board import Board
from src.message import Message as message


class Game:
    def __init__(self):
        self.board = Board()
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
        if self.board.is_full(total_marks_on_board, self.game_board):
            message.display_game_over_message(self)
        else:
            message.display_prompt_message_for_move(self, current_player)

    def process_user_input(self):
        user_input_as_string = self.get_user_input()
        position_choice = self.convert_input_to_integer(user_input_as_string)
        if self.board.is_spot_taken(self.game_board, position_choice):
            message.display_spot_taken_message(self)
            self.process_user_input()
        self.board.mark_board(
            position_choice,
            self.game_board,
            self.get_current_player(self.total_marks_on_board),
        )
        self.total_marks_on_board = self.board.count_marks(self.game_board)
        return self.game_board

    def convert_input_to_integer(self, user_input):
        return int(user_input)

    def get_user_input(self):
        user_input = input()
        return user_input

    def is_winner(self, game_board):

        if (
            self.board.is_winner_horizontal(game_board)
            or self.board.is_winner_vertical(game_board)
            or self.board.is_winner_diagonal(game_board)
        ):
            return True
        else:
            return False

    def determine_winner(self, total_marks_on_board):
        player = self.get_current_player(total_marks_on_board)
        if player == "X":
            return "O"
        else:
            return "X"

    def play_game(self):
        total_marks_on_board = self.board.count_marks(self.game_board)
        while not self.board.is_full(total_marks_on_board, self.game_board):
            self.get_prompt(total_marks_on_board)
            self.process_user_input()
            total_marks_on_board = self.board.count_marks(self.game_board)
            self.get_formatted_board()
            if self.is_winner(self.game_board):
                winner = self.determine_winner(total_marks_on_board)
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
