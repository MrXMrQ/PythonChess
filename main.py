#Tests for figures
from Test import Test_Figures

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
    print(figures)
    testing_area: Test_Figures = Test_Figures(figures[0], figures[1])
    testing_area.pawn_test()

figures: Figure = fill_figures()

start_test()