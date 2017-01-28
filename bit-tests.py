piece = 19
used = 32

print piece & used

print int('01');

board = int('111110011111', 2)
piece = int('11', 2)

available_spot = bin(board)[2:].find('0')
piece_position = piece << available_spot

print bin(board + piece_position)