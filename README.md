# A Python TicTacToe game with unbeatable AI

## Demo
```	python
Welcome to the game Tic Tac Toe!

Game mode selection:

1. Single Player Mode
2. Versus Mode
3. Spectator Mode (CPU vs CPU)

Your choice is (Enter the number): 1

Setting up the game...


Please enter your name: Steven

Token Selection:
A token is a letter (A to Z) that will be used to mark your moves on the board.

Please enter the token of your choice: S

The token for 'Steven' is 'S'
The token for 'COMP' is 'C'

Turn Selection:
You can choose to go first or let the other player go first.

Steven will pick which player goes first.

Would you like to go first or last, Steven? (Enter number):

1. Go first
2. Go last

Your choice is: 1

Steven will go first.

```

## Installation

Just Clone this repo and run ```python game.py```

## Dependencies

None, pure python code.


## Unbeatable AI
``` python

     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9

Steven, please make a move on the board (1 - 9): 2

       | S |
    -----------
       |   |
    -----------
       |   |


     C | S |
    -----------
       |   |
    -----------
       |   |

Steven, please make a move on the board (1 - 9): 5

     C | S |
    -----------
       | S |
    -----------
       |   |

     C | S |
    -----------
       | S |
    -----------
       | C |

Steven, please make a move on the board (1 - 9): 3

      C | S | S
     -----------
        | S |
     -----------
        | C |


      C | S | S
     -----------
        | S |
     -----------
      C | C |

...

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
