class Solution:
    def __init__(self):
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
    def draw_piece_in_board(self, character, new_piece, old_board):
        return ''

    @staticmethod
    def find_next_place(board):
        return board.rfind('1')

    @staticmethod
    def replace_place_in_string_character(evaluating_string, character, place):
        return evaluating_string.replace()

    @staticmethod
    def int_to_binary_string(board_int):
        binary = bin(board_int)[2::]
        return binary

    @staticmethod
    def draw_board(board, line_length):
        # Reverse the board so it represents the solution correctly
        board = board[::-1]

        board_lines = [board[i:i+line_length] for i in range(0, len(board), line_length)]

        # Draw a space between the characters to make them more visible
        for line_index, line in enumerate(board_lines):
            board_lines[line_index] = line.replace("", " ")[:-1]

        return "\n".join(board_lines)
