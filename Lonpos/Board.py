import math
from Lonpos.Functions import *

class Board:
    """
    Return the integer value for a 9x9 playboard.

    X X X X X X X X X X X
    X - - - - - - X X X X
    X - - - - - - - X X X
    X - - - - - - - - X X
    X - - X - - - - - - X
    X - - - - - - - - - X
    X - - - - - - - X X X
    X X - - - - - X X X X
    X X X - - - X X X X X
    X X X X - - X X X X X
    X X X X X X X X X X X

    :return int
    """
    def board_9x9(self):
        return {'board': reversed_binary_string_into_integer(
                "11111111111" +
                "10000001111" +
                "10000000111" +
                "10000000011" +
                "10010000001" +
                "10000000001" +
                "10000000111" +
                "11000001111" +
                "11100011111" +
                "11110011111" +
                "11111111111"),
            'line_length': 11
        }

    def number_of_steps(self, board):
        return int(math.log(board, 2))