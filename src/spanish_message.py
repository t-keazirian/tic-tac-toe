from symtable import Symbol
from src.symbol import SymbolOptions


class SpanishMessage:
    def welcome_message(self):
        return "Bienvenidos a Tic Tac Toe"

    def menu(self):
        return """
Elija una de las siguientes opciones:
1. Juega con los símbolos "X" y "O"
2. Elige tus propios símbolos
"""

    def display_symbols(self):
        symbols = SymbolOptions().symbols
        return f"Ingrese un número para elegir el símbolo asociado de esta lista: \n{symbols}"

    def invalid_menu_input(self):
        return "Ese ingreso no es válido. Por favor ingrese 1 o 2."

    def invalid_symbol_option(self):
        return "Ese ingreso no es válido. Por favor ingrese un número del 1 al 10."

    def choose_symbol_player_one(self):
        return "Jugador uno: elija su marca"

    def choose_symbol_player_two(self):
        return "Jugador dos: elija su marca"

    def rules(self):
        rules = """
Juega este juego tomando turnos marcando el tablero.
Cuando se le solicite, escriba un número entre 1 y 9 y presione enter.
Si ese lugar está ocupado, la computadora le pedirá que elija otra opción.
¡El primer jugador que obtiene tres de sus marcas seguidas gana!
Si el tablero está lleno y ninguno de los jugadores tiene tres marcas seguidas, es un empate y el juego termina.
Al final de cada juego, tendrás la opción de jugar de nuevo o salir.
"""
        return rules

    def game_over_message(self):
        return "Se acabó el juego: ¡empate!"

    def prompt_for_move(self, current_player):
        return (
            f"Jugador {current_player.mark} - escriba un número para marcar el tablero"
        )

    def declare_winner(self, winner):
        return f"Felicidades Jugador {winner} - ¡ganaste!"

    def invalid_board_input(self):
        return "Esa elección es incorrecta. Ingrese un número entre 1 y 9 para un lugar que no está ocupado."

    def play_again_prompt(self):
        return "¿Quieres jugar de nuevo? (Y/N)"

    def goodbye_message(self):
        return "¡Gracias por jugar - adios!"

    def invalid_repeat_game_input(self):
        return (
            "Esa elección es incorrecta. Ingrese Y para jugar de nuevo o N para salir."
        )

    def choose_players(self):
        return """
Por favor, haga una selección de las opciones:
1. Humano contra humano (2 jugadores)
2. Humano contra computadora (1 jugador)
3. Humano vs computadora imbatible (1 jugador)
"""

    def computer_go_first(self):
        return """🚨 ¡La computadora irá primero! 🚨

Estas son las reglas:
"""

    def human_go_first(self):
        return """🚨 ¡Irás primero! 🚨

Estas son las reglas:
"""
