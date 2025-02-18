from tkinter import Tk, Label

from Pieces.limited_range_piece import LimitedRangePiece
from Pieces.piece import Piece
from Pieces.pawn import Pawn
from Pieces.king import King
from Pieces.rook import Rook

from GUI.custom_button import CustomButton
from GUI.chessboard import Chessboard


def fill_figures() -> list:
    rooks = [Piece("♖", (1,1), [(1, 0), (-1, 0), (0, 1), (0, -1)]), 
             Rook("♖", (1,8), [(1, 0), (-1, 0), (0, 1), (0, -1)]),
             Piece("♜", (8,1), [(1, 0), (-1, 0), (0, 1), (0, -1)], "black"), 
             Rook("♜", (8,8), [(1, 0), (-1, 0), (0, 1), (0, -1)], "black")
            ]
    bishop = [Piece("♗", (1,3), [(1, -1), (1, 1), (-1,-1), (-1,1)]), 
              Piece("♗", (1,6), [(1, -1), (1, 1), (-1,-1), (-1,1)]),
              Piece("♝", (8,3), [(1, -1), (1, 1), (-1,-1), (-1,1)], "black"),
              Piece("♝", (8,6), [(1, -1), (1, 1), (-1,-1), (-1,1)], "black")
            ]
    queen = [Piece("♕", (1,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)]),
             Piece("♛", (8,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], "black")
            ]
    knight = [LimitedRangePiece("♘", (1,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)]), 
              LimitedRangePiece("♘", (1,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)]),
              LimitedRangePiece("♞", (8,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], "black"),
              LimitedRangePiece("♞", (8,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], "black")
             ]
    king = [King("♔", (1,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)]),
            King("♚", (8,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)], "black")]

    pawns = []
    for i in range(8):
        pawns.append(Pawn("♙", (2, i+1), [(1,0)]))
        pawns.append(Pawn("♟", (7, i+1), [(-1,0)], "black"))

    pieces: Piece = [rooks, bishop, queen, knight, king, pawns]

    return pieces

def create_label(window, row, col, text="", bg_color="white", fg_color="black") -> None:
    label = Label(window, text=text, bg=bg_color, fg=fg_color, font=('Helvetica 20 bold'))
    label.grid(row=row, column=col, sticky="nsew")

def create_window(cc) -> Tk:
    window = Tk()
    window.title("PyChess")
    window.resizable(False,False)

    # Configure the grid layout to make rows and columns expandable
    for i in range(9):
        window.grid_rowconfigure(i, weight=1, uniform="equal")
        window.grid_columnconfigure(i, weight=1, uniform="equal")

    # Add row and column labels (numbers) for the chessboard
    for i in range(9):
        for j in range(9):
            if i == 8 and j < 8:  # Bottom row (numbers)
                create_label(window, i, j + 1, text=f"{j + 1}")
            elif j == 0 and i < 8:  # Left column (numbers)
                create_label(window, i, j, text=f"{8 - i}")

    # Add the chessboard pieces as buttons (Custom_Button is assumed to be defined elsewhere)
    for position, piece in Chessboard.chessboard.items():
        CustomButton(piece, cc, window, position)

    return window

pieces: Piece = fill_figures()
cc = Chessboard(pieces)
window = create_window(cc)

print(cc)

for piece in pieces[5]:
    piece.window = window

window.mainloop()