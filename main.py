# Pieces
from Pieces.MyPiece import Piece

# Chessboard
from tkinter import *
from GUI.Chessboard.MyChessboard import Chessboard

def fill_figures() -> list:
    pieces: Piece = []
    pieces.append(Piece("Rook 1", (1,1), [(1, 0), (-1, 0), (0, 1), (0, -1)], True))
    pieces.append(Piece("Rook 2", (1,8), [(1, 0), (-1, 0), (0, 1), (0, -1)], True))
    pieces.append(Piece("Bishop 1", (1,3), [(1, -1), (1, 1), (-1,-1), (-1,1)], True))
    pieces.append(Piece("Bishop 1", (1,6), [(1, -1), (1, 1), (-1,-1), (-1,1)], True))
    pieces.append(Piece("Queen", (1,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], True))

    pieces.append(Piece("Knight 1", (1,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], True, True))
    pieces.append(Piece("Knight 1", (1,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], True, True))
    
    pieces.append(Piece("King", (1,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)], True, True))

    pieces.append(Piece("Enemy", (5,5), [(0,0)], False))

    for i in range(8):
        pieces.append(Piece("Pawn {}".format(i + 1), (2,i + 1), [(1, 0)], True, True, True))

    return pieces

pieces: Piece = fill_figures()
chessboard = Chessboard(pieces)

window = chessboard.create_window()
window.mainloop()