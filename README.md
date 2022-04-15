# Tic Tac Toe with Python

## This project allows you to play the game Tic Tac Toe from the command line.

## Setup
This game uses `pynev` to manage python version
```
brew install pyenv
```

This game uses `python 3.1.0`

## To Play the Game:
* Type `python tic_tac_toe.py` into your command line prompt while in this repo's directory.
* The game will go through a series of prompts for a two-player TTT game.
* You will be notified if you input an incorrect value and be re-prompted to correct the value.
* The game will declare a winner and gives the option to play again.

### Testing:
This project uses [unittest](https://docs.python.org/3/library/unittest.html), a Python testing framework.

#### To run the tests:
`python -m unittest -v`

#### Code Coverage:
We are using [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/) for code coverage

`pip install coverage`

To Run:
`coverage -m unittest -v`

Generate HTML report:
`coverage html`

This will generate an HTML report and folder that where you can view the report.
