# A Python TicTacToe game with unbeatable AI

## Change Log
```
v1.5

- Heavily refactored the game class and split it into multiple classes to make the project more modular.
- Improved game menu.
- Improved overall UI to make game play easier.
- Improved system feedbacks to notify player next in line of last move and who makes the move.
- Added tests for each module.  
- Updated comments to make code easier to reason about.

```

```
v1.0

- Initial release

```

## Installation

Just Clone this repo and run ```python game.py```

## Dependencies

None, pure python code.

## Files

```
- board.py
- player.py
- human.py
- cpu.py
- game.py
- util.py

Optional Files - (For Development)

- board_tests.py
- human_tests.py
- cpu_tests.py
- game_tests.py
- util_tests.py

```

## Demo
```
Welcome to Tic Tac Toe Classic!

Select a game mode:

1. Play against a super computer
2. Play with a friend
3. Spectate a game (CPU vs CPU)

Your choice is (Enter the number): 1

...

Please enter your name: Steven

Select a token:
A token is a letter (A to Z) that will be used to mark your moves on the board.

Please enter the token of your choice: S

...

The token for 'Steven' is 'S'
The token for 'COMP' is 'C'

Select turn:
You can choose to go first or let the other player go first.

Steven will pick which player goes first.

Would you like to go first or last, Steven? (Enter number):

1. Go first
2. Go last

Your choice is: 1

Steven will go first.
Iris (AI) will go last.

...

```

## Unbeatable AI
```
  1  |  2  |  3
-----------------
  4  |  5  |  6
-----------------
  7  |  8  |  9

Steven, please make a move on the board (1 - 9):


  S  |  2  |  3
-----------------
  4  |  5  |  6
-----------------
  7  |  8  |  9


'Steven (S)' chose spot '1'

  S  |  2  |  3
-----------------
  4  |  U  |  6
-----------------
  7  |  8  |  9


'Iris (AI) (U)' chose spot '5'
Steven, please make a move on the board (1 - 9):


  S  |  S  |  3
-----------------
  U  |  U  |  U
-----------------
  S  |  8  |  9


'Iris (AI) (U)' chose spot '6'

Iris (AI) win!

```

## License
MIT License

Copyright (c) 2018 Steven Tuetpiu Kwok

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
