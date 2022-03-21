class Game:
    #    def __init__(self):
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player_one = "X"
    player_two = "O"
    play_count = 0

    def get_welcome_message(self):
        return "Welcome to Tic Tac Toe"

    def initialize_board(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def count_plays(self):
        for mark in self.board:
            play_count = self.board.count(self.player_one) + self.board.count(
                self.player_two
            )
        return play_count

    def get_next_player(self, play_count):
        if play_count == 0:
            return self.player_one
        elif play_count % 2 == 0:
            return self.player_one
        else:
            return self.player_two

    def get_prompt(self, play_count):
        next_player = self.get_next_player(play_count)
        if play_count == len(self.board):
            prompt = "Game Over!"
        else:
            prompt = f"Player {next_player} - enter a number to place your mark"
        return prompt

    def place_mark_on_board(self, user_input, board, play_count):
        input_index = user_input - 1
        board[input_index] = self.get_next_player(play_count)
        return board

    def process_user_input(self):
        position_choice = int(input())
        self.place_mark_on_board(position_choice, self.board, self.play_count)
        print(self.initialize_board())

    def progress_game(self):
        self.get_prompt(self.play_count)
        current_play_count = self.count_plays()
        while current_play_count < len(self.board):
            print(self.get_prompt(current_play_count))
            print(f"{current_play_count} current play count")
            print(self.get_next_player(current_play_count))
            self.process_user_input()
            current_play_count += 1

    def is_spot_taken(self, user_input, board):
        input_index = user_input - 1
        if (self.player_one or self.player_two) not in board[input_index]:
            return False
        else:
            return True

    def run(self):
        print(self.get_welcome_message())
        print(self.initialize_board())
        # print(self.get_prompt(self.count_plays()))
        self.progress_game()
