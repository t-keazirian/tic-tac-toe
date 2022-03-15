class Game:

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def get_welcome_message(self):
        return "Welcome to Tic Tac Toe"

    def initialize_board(self):
        return f"{self.board[0]} | {self.board[1]} | {self.board[2]}\n--+--+--\n{self.board[3]} | {self.board[4]} | {self.board[5]}\n--+--+--\n{self.board[6]} | {self.board[7]} | {self.board[8]}"

    def count_plays(self):
        play_count = self.board.count("X") + self.board.count("O")
        return play_count

    def get_next_player(self, number):
        if number == 0:
            return "X"
        elif number % 2 == 0:
            return "X"
        else:
            return "O"

    def get_prompt(self, play_count):
        next_player = self.get_next_player(play_count)
        if play_count == 9:
            prompt = "Game Over!"
        else:
            prompt = f"Player {next_player} - enter the number of an empty spot"
        return prompt

    def place_mark_on_board(self, user_input):
        user_input = user_input - 1
        self.board[user_input] = self.get_next_player(self.count_plays())
        return self.board

    # def place_mark_on_board(self, get_next_player):
    # position_choice = input()
    # position_choice = int(position_choice) - 1
    #        position_choice = 0
    #        self.board[position_choice] = self.get_next_player(0)

    def run(self):
        print(self.get_welcome_message())
        print(self.initialize_board())
        print(self.get_prompt(self.count_plays()))
