# Pieces
from Pieces.piece import Piece
from Pieces.pawn import Pawn
from Pieces.limited_range_piece import LimitedRangePiece

from GUI.chessboard import Chessboard

def fill_figures() -> list:
    rooks = [Piece("♖", (1,1), [(1, 0), (-1, 0), (0, 1), (0, -1)]), 
             Piece("♖", (1,8), [(1, 0), (-1, 0), (0, 1), (0, -1)]),
             Piece("♜", (8,1), [(1, 0), (-1, 0), (0, 1), (0, -1)], False), 
             Piece("♜", (8,8), [(1, 0), (-1, 0), (0, 1), (0, -1)], False)
            ]
    bishop = [Piece("♗", (1,3), [(1, -1), (1, 1), (-1,-1), (-1,1)]), 
              Piece("♗", (1,6), [(1, -1), (1, 1), (-1,-1), (-1,1)]),
              Piece("♝", (8,3), [(1, -1), (1, 1), (-1,-1), (-1,1)], False),
              Piece("♝", (8,6), [(1, -1), (1, 1), (-1,-1), (-1,1)], False)
            ]
    queen = [Piece("♕", (1,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)]),
             Piece("♛", (8,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], False)
            ]
    knight = [LimitedRangePiece("♘", (1,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)]), 
              LimitedRangePiece("♘", (1,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)]),
              LimitedRangePiece("♞", (8,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], False),
              LimitedRangePiece("♞", (8,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], False)
             ]
    king = [LimitedRangePiece("♔", (1,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)]),
            LimitedRangePiece("♚", (8,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)], False)]

    pawns = []
    for i in range(8):
        pawns.append(Pawn("♙", (2, i+1), [(1,0)]))
        pawns.append(Pawn("♟", (7, i+1), [(-1,-1)], False))

    pieces: Piece = [rooks, bishop, queen, knight, king, pawns]

    return pieces

pieces: Piece = fill_figures()
chessboard = Chessboard(pieces)

window = chessboard.create_window()

for piece in pieces[5]:
    piece.window = window

window.mainloop()