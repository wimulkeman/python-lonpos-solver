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
    @staticmethod
    def board_9x9():
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

    @staticmethod
    def board_5x11():
        return {'board': reversed_binary_string_into_integer(
            "1111111111111" +
            "1000000000001" +
            "1000000000001" +
            "1000000000001" +
            "1000000000001" +
            "1000000000001" +
            "1111111111111"),
            'line_length': 13
        }

    @staticmethod
    def number_of_steps(board):
        return int(math.log(board, 2))