from Lonpos import Board, Piece, Solution

# Get the board on witch there will be played
board = Board.Board()
play_board = board.board_9x9()

# Generate the pieces for the board
pieces = Piece.Piece(play_board['line_length'])

# Keep track of the generated solutions
solution = Solution.Solution()
solution.set_board(play_board['board'])

found_solutions = 0

# Use the total board length to calculate the first available spot in reverse
total_board_length = len(bin(play_board['board'])[2:])

for label, piece in pieces.get_pieces().iteritems():
    # Get the last 0 in the bit string which indicates a free spot
    available_spot = bin(solution.get_board())[2:].rfind('0')
    if not available_spot:
        break
    available_spot = total_board_length - available_spot - 1

    # Check if one of the positions of the piece fits into the free spots.
    for piece_position in piece:
        new_position = piece_position << available_spot
        if solution.does_piece_fit(new_position):
            print 'fit'
            solution.add_piece(new_position)
            break
        else:
            continue

print board.board_9x9()['board']
print bin(board.board_9x9()['board'])
print solution.get_board()
print bin(solution.get_board())
