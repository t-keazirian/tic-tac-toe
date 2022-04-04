class Message:
    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe")

    def display_game_over_message(self):
        print("Game Over!")

    def display_prompt_message_for_move(self, current_player):
        print(f"Player {current_player} - enter a number to place your mark")

    def display_error_prompt_for_occupied_spot(self):
        print("Spot is taken - choose another spot")

    def display_formatted_board(self, board):
        print(
            f"{board[0]} | {board[1]} | {board[2]}\n--+--+--\n{board[3]} | {board[4]} | {board[5]}\n--+--+--\n{board[6]} | {board[7]} | {board[8]}"
        )

    def display_spot_taken_message(self):
        print("Spot is taken - please choose another spot")

    def display_winner_message(self, winner):
        print(f"Congrats Player {winner} - you are the winner!")

    def display_incorrect_input_message(self):
        print("That input is incorrect.\nPlease input a number 1-9.")
