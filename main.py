#Tests for figures
from Test import Test_Figures

#Chessboard
from MyChessboard import Chessboard

#Chess pieces
from MyFigure import Figure
from MyPawn import Pawn
from MyRook import Rook

def fill_figures() -> list:
    pawns: Pawn = []
    for i in range(8):
        pawns.append(Pawn("Pawn {}".format(i + 1), (i + 1,2)))

    rooks: Rook = [Rook("Rook0", (1,1)), Rook("Rook1", (8,1))]
        
    return[pawns, rooks]

def start_test():
    print(pieces)
    testing_area: Test_Figures = Test_Figures(pieces[0], pieces[1])
    testing_area.pawn_test()
    testing_area.rook_test()

pieces: Figure = fill_figures()
board = Chessboard(pieces)
board.print_formated_chessboard()