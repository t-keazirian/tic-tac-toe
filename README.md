# Tic Tac Toe with Python

## This project allows you to play the game Tic Tac Toe from the command line.

## Setup

This game uses `pynev` to manage python version

```
brew install pyenv
```

This game uses `python 3.1.0`

## To Play the Game:

- Type `python tic_tac_toe.py` into your command line prompt while in this repo's directory.
- The game will go through a series of prompts for a two-player TTT game.
- You will be notified if you input an incorrect value and be re-prompted to correct the value.
- The game will declare a winner and give the option to play again.

## Testing:

This project uses [unittest][1], a Python testing framework.

This project also uses [pytest][2] for acceptance testing.

### To run the tests:

```
python -m unittest -v
```

### To run tests with `pytest` (this command will also run the unit-tests)

```
pytest test
```

### Code Coverage:

We are using [Coverage.py][3] for code coverage

```
pip install coverage
```

### To Run:

```
coverage -m unittest -v
```

### Generate HTML report:

```
coverage html
```

This will generate an HTML report and folder where you can view the report.

[1]: https://docs.python.org/3/library/unittest.html
[2]: https://docs.pytest.org/en/7.1.x/index.html
[3]: https://coverage.readthedocs.io/en/6.3.2/
