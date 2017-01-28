from Lonpos.Functions import *

class Piece:
    def __init__(self, line_length):
        """
        A: 8 possible positions

        // . . . .
        // . A . .
        // . A . .
        // . A A .
        // . . . .

        B: 8 possible positions

        // . . . .
        // . . B .
        // . B B .
        // . B B .
        // . . . .

        C: 8 possible positions

        // . . . .
        // . C . .
        // . C . .
        // . C . .
        // . C C .
        // . . . .

        D: 8 possible possitions

        // . . . .
        // . D . .
        // . D . .
        // . D D .
        // . D . .
        // . . . .

        E: 8 possible possitions

        // . . . .
        // . E . .
        // . E . .
        // . E E .
        // . . E .
        // . . . .

        F: 4 possible positions

        // . . . .
        // . F . .
        // . F F .
        // . . . .

        G: 4 possible positions

        // . . . . .
        // . G . . .
        // . G . . .
        // . G G G .
        // . . . . .

        H: 4 possible positions

        // . . . . .
        // . H . . .
        // . H H . .
        // . . H H .
        // . . . . .

        I: 4 possible positions

        // . . . .
        // . I I .
        // . I . .
        // . I I .
        // . . . .

        J: 2 possible positions

        // . . .
        // . J .
        // . J .
        // . J .
        // . J .
        // . . .

        K: 1 possible position

        // . . . .
        // . K K .
        // . K K .
        // . . . .

        L: 1 possible position

        // . . . . .
        // . . L . .
        // . L L L .
        // . . L . .
        // . . . . .
        """
        self.pieces = {
            'A': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "11"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 3)) + "1"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "111"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 3)) + "111")
            ],
            'B': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 2)) + "1"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 3)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "111"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 3)) + "111")
            ],
            'C': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "11"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1111" + ("0" * (line_length - 4)) + "1"),
                reversed_binary_string_into_integer("1111" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1111"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 4)) + "1111")
            ],
            'D': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 2)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 2)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1111" + ("0" * (line_length - 3)) + "1"),
                reversed_binary_string_into_integer("1111" + ("0" * (line_length - 2)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "1111"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 3)) + "1111")
            ],
            'E': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 2)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 2)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 1)) + "11"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 4)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 1)) + "111"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 4)) + "111")
            ],
            'F': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "11"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "1"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 1)) + "1")
            ],
            'G': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "111"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 3)) + "111"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 3)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1")
            ],
            'H': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 1)) + "11"),
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "11" + ("0" * (line_length - 3)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 3)) + "11" + ("0" * (line_length - 2)) + "1"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 1)) + "11" + ("0" * (line_length - 1)) + "1")
            ],
            'I': [
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "1" + ("0" * (line_length - 1)) + "11"),
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 2)) + "11"),
                reversed_binary_string_into_integer("111" + ("0" * (line_length - 3)) + "101"),
                reversed_binary_string_into_integer("101" + ("0" * (line_length - 3)) + "111")
            ],
            'J': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1" + ("0" * (line_length - 1)) + "1"),
                reversed_binary_string_into_integer("1111")
            ],
            'K': [
                reversed_binary_string_into_integer("11" + ("0" * (line_length - 2)) + "11")
            ],
            'L': [
                reversed_binary_string_into_integer("1" + ("0" * (line_length - 2)) + "111" + ("0" * (line_length - 2)) + "1")
            ]
        }

    def get_pieces(self):
        return self.pieces
