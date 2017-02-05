from Lonpos import Board, Piece, Solution
from timeit import default_timer as timer
import datetime
import multiprocessing
from functools import partial

# Get the board on witch there will be played
board = Board.Board()
# play_board = board.board_5x11()
play_board = board.board_9x9()

# Generate the pieces for the board
available_pieces = Piece.Piece(play_board['line_length'])

found_solutions = 0

# Use the total board length to calculate the first available spot in reverse
total_board_length = len(bin(play_board['board'])[2:])


def calculate_solution(filled_board, pieces, new_board_solution, solution_instance, piece_character=None):
    # Get the last 0 in the bit string which indicates a free spot
    available_spot = bin(filled_board['board'])[2:].rfind('0')
    if not available_spot:
        return

    # When the function is called without any
    if not pieces:
        print ' ======= Solution ======= '
        print solution_instance.draw_board(new_board_solution, filled_board['line_length'])
        print ' ======================== '
        return

    available_spot = total_board_length - available_spot - 1

    for label, piece in pieces.iteritems():
        # Using this check it is possible to only process one character for the starting position
        # of the board
        if piece_character is not None and piece_character is not label:
            continue

        # Check if one of the positions of the piece fits into the free spots.
        for piece_position in piece:
            new_position = piece_position << available_spot
            if (filled_board['board'] & new_position) == 0:
                # Add the character to the board
                new_board_solution = solution.draw_piece_in_board(label, new_position, filled_board['board'], new_board_solution)

                # Create a new board by using the old board with the piece added to it
                new_board = filled_board.copy()
                new_board['board'] = filled_board['board'] + new_position
                # Look for the rest of the board with all the pieces which haven't been evaluated
                # yet
                new_pieces = pieces.copy()
                del new_pieces[label]

                calculate_solution(new_board, new_pieces, new_board_solution, solution_instance)


if __name__ == '__main__':
    solution = Solution.Solution()
    board_solution = solution.draw_start_board(play_board['board'])

    # Draw the board in starting position
    print '== The starting board =='
    print solution.draw_board(board_solution, play_board['line_length'])

    available_pieces_list = available_pieces.get_pieces()

    # Make a worker process for every core available
    # pool = multiprocessing.Pool(multiprocessing.cpu_count() + 4)
    pool = multiprocessing.Pool(len(available_pieces_list.keys()))

    start_time = timer()

    pool.map(
        partial(calculate_solution, play_board, available_pieces_list, board_solution, solution),
        available_pieces_list.keys()
    )
    pool.close()
    pool.join()

    end_time = timer()

    print str(datetime.timedelta(seconds=(end_time - start_time)))
