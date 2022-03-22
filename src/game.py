from src.board import Board


class Game:
    def __init__(self):
        # initialize a new Board
        self.new_board = Board()
        self.board = self.new_board.starter_board
        self.player_one = "X"
        self.player_two = "O"
        self.total_marks_on_board = 0

    def get_welcome_message(self):
        return "Welcome to Tic Tac Toe"

    def get_formatted_board(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def get_prompt(self, total_marks_on_board):
        current_player = self.new_board.get_current_player(total_marks_on_board)
        if total_marks_on_board == len(self.board):
            prompt = "Game Over!"
        else:
            prompt = f"Player {current_player} - enter a number to place your mark"
        return prompt

    def is_spot_taken(self, board, user_input):
        input_index = user_input - 1
        if (
            board[input_index] == self.player_one
            or board[input_index] == self.player_two
        ):
            return True
        else:
            return False

    def place_mark_on_board(self, user_input, board, total_marks_on_board):
        input_index = user_input - 1
        board[input_index] = self.new_board.get_current_player(total_marks_on_board)
        return board

    def process_user_input(self):
        position_choice = int(input())
        self.place_mark_on_board(position_choice, self.board, self.total_marks_on_board)
        self.total_marks_on_board += 1

    def progress_game(self):
        current_total_marks_on_board = self.new_board.count_marks_in_board(
            self.player_one, self.player_two
        )
        while current_total_marks_on_board != len(self.board):
            print(self.get_prompt(current_total_marks_on_board))
            self.process_user_input()
            current_total_marks_on_board += 1
            print(self.get_formatted_board())
        else:
            print(self.get_prompt(current_total_marks_on_board))

    def run(self):
        print(self.get_welcome_message())
        print(self.get_formatted_board())
        self.progress_game()
