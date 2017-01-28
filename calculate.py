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

for label, piece in pieces.get_pieces().iteritems():
    available_spot = bin(solution.get_board())[2:].find('0')
    if not available_spot:
        break

    for piece_position in piece:
        piece_position << available_spot
        if solution.does_piece_fit(piece_position):
            print 'fit'
            solution.add_piece(piece_position)
            break
        else:
            continue

print board.board_9x9()['board']
print bin(board.board_9x9()['board'])
print solution.get_board()
print bin(solution.get_board())
