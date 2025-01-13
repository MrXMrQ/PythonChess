# Pieces
from Pieces.MyPiece import Piece
from Pieces.MyPawn import Pawn
from Pieces.MyRook import Rook
from Pieces.MyBishop import Bishop
from Pieces.MyQueen import Queen
from Pieces.MyKing import King

# Chessboard
from tkinter import *
from GUI.Chessboard.MyChessboard import Chessboard

def fill_figures() -> list:
    pawns: Pawn = []
    for i in range(8):
        pawns.append(Pawn("Pawn {}".format(i + 1), (2,i + 1)))

    rooks: Rook = []
    rooks.append(Rook("Rook 1", (1,1)))
    rooks.append(Rook("Rook 2", (1,8)))

    bishop: Bishop = []
    bishop.append(Bishop("Bishop 1", (1,3)))
    bishop.append(Bishop("Bishop 1", (1,6)))

    return[pawns, rooks, bishop, [Queen("Queen", (1,4))], [King("King", (1,5))]]

pieces: Piece = fill_figures()
chessboard = Chessboard(pieces)

window = chessboard.create_window()
window.mainloop()