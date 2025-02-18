# Pieces
from Pieces.piece import Piece
from Pieces.pawn import Pawn
from Pieces.limited_range_piece import LimitedRangePiece

from GUI.chessboard import Chessboard

def fill_figures() -> list:
    rooks = [Piece("♖", (1,1), [(1, 0), (-1, 0), (0, 1), (0, -1)]), Piece("♖", (1,8), [(1, 0), (-1, 0), (0, 1), (0, -1)])]
    bishop = [Piece("♗", (1,3), [(1, -1), (1, 1), (-1,-1), (-1,1)]), Piece("♗", (1,6), [(1, -1), (1, 1), (-1,-1), (-1,1)])]
    queen = [Piece("♕", (1,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)])]
    knight = [LimitedRangePiece("♘", (1,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)]), LimitedRangePiece("♘", (1,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)])]
    king = [LimitedRangePiece("♔", (1,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)])]

    pawns = []
    for i in range(8):
        pawns.append(Pawn("♙", (2, i+1), [(1,0)], True))

    pieces: Piece = [rooks, bishop, queen, knight, king, pawns]
    pieces.append([Piece("♟", (5,5), [(0,0)], False)])

    return pieces

pieces: Piece = fill_figures()
chessboard = Chessboard(pieces)

window = chessboard.create_window()

for piece in pieces[5]:
    piece.window = window

window.mainloop()