class Solution:
    def __init__(self):
        self.board = 0
        return

    def does_piece_fit(self, piece):
        return (self.board & piece) == 0

    def add_piece(self, piece):
        print piece
        self.board = self.board + piece
        return self

    def set_board(self, board):
        self.board = board
        return self

    def get_board(self):
        return self.board
