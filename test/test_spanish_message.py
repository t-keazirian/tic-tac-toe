import unittest

from src.spanish_message import SpanishMessage
from src.symbol import SymbolOptions


class TestSpanishMessage(unittest.TestCase):
    def test_welcome_message_prints_to_console(self):
        spanish_message = SpanishMessage()
        expected_message = "Bienvenidos a Tic Tac Toe"
        actual_message = spanish_message.welcome_message()
        self.assertEqual(expected_message, actual_message)

    def test_menu_returns_menu_for_symbol_options(self):
        spanish_message = SpanishMessage()
        expected_message = """
Elija una de las siguientes opciones:
1. Juega con los símbolos "X" y "O"
2. Elige tus propios símbolos
"""
        actual_message = spanish_message.menu()
        self.assertEqual(expected_message, actual_message)

    def test_display_symbols_displays_symbols_and_message(self):
        spanish_message = SpanishMessage()
        symbols = SymbolOptions().symbols

        expected_message = f"Ingrese un número para elegir el símbolo asociado de esta lista: \n{symbols}"
        actual_message = spanish_message.display_symbols()
        self.assertEqual(expected_message, actual_message)

    def test_invalid_menu_input_prints_message(self):
        spanish_message = SpanishMessage()
        expected_message = "Ese ingreso no es válido. Por favor ingrese 1 o 2."
        actual_message = spanish_message.invalid_menu_input()
        self.assertEqual(expected_message, actual_message)

    def test_invalid_symbol_options_prints_message(self):
        spanish_message = SpanishMessage()
        expected_message = (
            "Ese ingreso no es válido. Por favor ingrese un número del 1 al 10."
        )
        actual_message = spanish_message.invalid_symbol_option()
        self.assertEqual(expected_message, actual_message)

    def test_choose_symbol_player_one_prints_message(self):
        spanish_message = SpanishMessage()
        expected_message = "Jugador uno: elija su marca"
        actual_message = spanish_message.choose_symbol_player_one()
        self.assertEqual(expected_message, actual_message)

    def test_choose_symbol_player_two_prints_message(self):
        spanish_message = SpanishMessage()
        expected_message = "Jugador dos: elija su marca"
        actual_message = spanish_message.choose_symbol_player_two()
        self.assertEqual(expected_message, actual_message)

    def test_game_over_prints_to_console(self):
        spanish_message = SpanishMessage()
        expected_message = "Se acabó el juego: ¡empate!"
        actual_message = spanish_message.game_over_message()
        self.assertEqual(expected_message, actual_message)

    def test_X_player_is_prompted_for_move_when_is_current_player(self):
        spanish_message = SpanishMessage()
        current_player = "X"
        expected_message = (
            f"Jugador {current_player} - escriba un número para marcar el tablero"
        )
        actual_message = spanish_message.prompt_for_move(current_player)
        self.assertEqual(expected_message, actual_message)

    def test_declare_winner_with_correct_mark_as_winner(self):
        spanish_message = SpanishMessage()
        winner = "X"
        expected_message = f"Felicidades Jugador {winner} - ¡ganaste!"
        actual_message = spanish_message.declare_winner(winner)
        self.assertEqual(expected_message, actual_message)

    def test_invalid_board_input(self):
        spanish_message = SpanishMessage()
        expected_message = "Esa elección es incorrecta. Ingrese un número entre 1 y 9 para un lugar que no está ocupado."
        actual_message = spanish_message.invalid_board_input()
        self.assertEqual(expected_message, actual_message)

    def test_play_again_prompt(self):
        spanish_message = SpanishMessage()
        expected_message = "¿Quieres jugar de nuevo? (Y/N)"
        actual_message = spanish_message.play_again_prompt()
        self.assertEqual(expected_message, actual_message)

    def test_goodbye_message(self):
        spanish_message = SpanishMessage()
        expected_message = "¡Gracias por jugar - adios!"
        actual_message = spanish_message.goodbye_message()
        self.assertEqual(expected_message, actual_message)

    def test_invalid_repeat_game_message(self):
        spanish_message = SpanishMessage()
        expected_message = (
            "Esa elección es incorrecta. Ingrese Y para jugar de nuevo o N para salir."
        )
        actual_message = spanish_message.invalid_repeat_game_input()
        self.assertEqual(expected_message, actual_message)

    def test_rules_prints_to_console(self):
        spanish_message = SpanishMessage()
        rules = """
Juega este juego tomando turnos marcando el tablero.
Cuando se le solicite, escriba un número entre 1 y 9 y presione enter.
Si ese lugar está ocupado, la computadora le pedirá que elija otra opción.
¡El primer jugador que obtiene tres de sus marcas seguidas gana!
Si el tablero está lleno y ninguno de los jugadores tiene tres marcas seguidas, es un empate y el juego termina.
Al final de cada juego, tendrás la opción de jugar de nuevo o salir.
"""
        actual_message = spanish_message.rules()
        self.assertEqual(rules, actual_message)

    def test_choose_players_prints_to_console(self):
        spanish_message = SpanishMessage()
        expected_message = """
Por favor, haga una selección de las opciones:
1. Humano contra humano (2 jugadores)
2. Humano contra computadora (1 jugador)
"""
        actual_message = spanish_message.choose_players()
        self.assertEqual(expected_message, actual_message)

    def test_computer_took_turn_prints_to_console(self):
        spanish_message = SpanishMessage()
        expected_message = "La computadora marcó el tablero"
        actual_message = spanish_message.computer_took_turn()
        self.assertEqual(expected_message, actual_message)
