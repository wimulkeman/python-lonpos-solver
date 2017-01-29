from Lonpos import Board, Piece, Solution

# Get the board on witch there will be played
board = Board.Board()
play_board = board.board_9x9()

# Generate the pieces for the board
available_pieces = Piece.Piece(play_board['line_length'])

# Keep track of the generated solutions
solution = Solution.Solution()
solution.set_board(play_board['board'])

found_solutions = 0

# Use the total board length to calculate the first available spot in reverse
total_board_length = len(bin(play_board['board'])[2:])

def calculate_solution(board, pieces):
    # When the function is called without any
    if not pieces:
        global found_solutions
        found_solutions = found_solutions + 1
        print "Solution found: " + str(found_solutions)
        return

    # Get the last 0 in the bit string which indicates a free spot
    available_spot = bin(board)[2:].rfind('0')
    if not available_spot:
        return

    available_spot = total_board_length - available_spot - 1

    for label, piece in pieces.iteritems():
        # Check if one of the positions of the piece fits into the free spots.
        for piece_position in piece:
            new_position = piece_position << available_spot
            if (board & new_position) == 0:
                # Create a new board by using the old board with the piece added to it
                new_board = board + new_position
                # Look for the rest of the board with all the pieces which haven't been evaluated
                # yet
                new_pieces = pieces.copy()
                del new_pieces[label]

                calculate_solution(new_board, new_pieces)

calculate_solution(play_board['board'], available_pieces.get_pieces())
