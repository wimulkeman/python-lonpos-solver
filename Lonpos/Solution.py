class Solution:
    def __init__(self):
        self.characters = {
            'A': '\x1b[0;35;40mB\x1b[0m',
            'B': '\x1b[0;34;40mB\x1b[0m',
            'C': '\x1b[0;36;40mC\x1b[0m',
            'D': '\x1b[1;33;40mD\x1b[0m',
            'E': '\x1b[0;37;40mE\x1b[0m',
            'F': '\x1b[1;32;40mF\x1b[0m',
            'G': '\x1b[1;35;40mG\x1b[0m',
            'H': '\x1b[0;32;40mH\x1b[0m',
            'I': '\x1b[0;33;40mI\x1b[0m',
            'J': '\x1b[0;31;40mJ\x1b[0m',
            'K': '\x1b[1;31;40mK\x1b[0m',
            'L': '\x1b[1;37;40mL\x1b[0m',
            'X': '\x1b[2;37;48mX\x1b[0m'
        }

        return

    """
    This function is used to draw the boundries of the board. It should only be used
    for the empty start board for it uses some other ways to deduce the spaces which
    needs to be filled.
    """
    def draw_start_board(self, board):
        binary_string = self.int_to_binary_string(board)
        filled_board = binary_string.replace('1', 'X')

        return filled_board

    """
    This function is used to draw partial solutions into a board.
    """
    def draw_piece_in_board(self, character, new_piece, current_board, solution_board):
        # Color the character
        color_character = self.characters[character]

        binary_board = self.int_to_binary_string(current_board)
        binary_piece = self.int_to_binary_string(new_piece)

        binary_piece = ((len(binary_board) - len(binary_piece)) * '0') + binary_piece

        character_position = self.find_next_place(binary_piece)
        while character_position is not -1:
            byte_solution_board = bytearray(solution_board)
            byte_solution_board[character_position] = character
            solution_board = str(byte_solution_board)

            byte_binary_piece = bytearray(binary_piece)
            byte_binary_piece[character_position] = '0'
            binary_piece = str(byte_binary_piece)

            character_position = self.find_next_place(binary_piece)

        return solution_board

    @staticmethod
    def find_next_place(board):
        return board.rfind('1')

    @staticmethod
    def int_to_binary_string(board_int):
        binary = bin(board_int)[2::]
        return binary

    def draw_board(self, board, line_length):
        # Reverse the board so it represents the solution correctly
        board = board[::-1]

        board_lines = [board[i:i+line_length] for i in range(0, len(board), line_length)]

        # Draw a space between the characters to make them more visible
        for line_index, line in enumerate(board_lines):
            line = line.replace("", " ")[:-1]

            for character, colored_character in self.characters.iteritems():
                line = line.replace(character, colored_character)

            board_lines[line_index] = line

        return "\n".join(board_lines)
