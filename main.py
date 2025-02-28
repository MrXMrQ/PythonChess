from tkinter import Frame, Tk, Label

from Pieces.knight import LimitedRangePiece
from Pieces.piece import Piece
from Pieces.pawn import Pawn
from Pieces.king import King
from Pieces.rook import Rook

from GUI.custom_banner import CustomBanner
from GUI.custom_button import CustomButton
from GUI.chessboard import Chessboard


def fill_figures() -> list:
    rooks = [Rook("♖", (1,1), [(1, 0), (-1, 0), (0, 1), (0, -1)], 5), 
             Rook("♖", (1,8), [(1, 0), (-1, 0), (0, 1), (0, -1)], 5),
             Rook("♜", (8,1), [(1, 0), (-1, 0), (0, 1), (0, -1)], 5, "black"), 
             Rook("♜", (8,8), [(1, 0), (-1, 0), (0, 1), (0, -1)], 5, "black")
            ]
    bishop = [Piece("♗", (1,3), [(1, -1), (1, 1), (-1,-1), (-1,1)], 3), 
              Piece("♗", (1,6), [(1, -1), (1, 1), (-1,-1), (-1,1)], 3),
              Piece("♝", (8,3), [(1, -1), (1, 1), (-1,-1), (-1,1)], 3, "black"),
              Piece("♝", (8,6), [(1, -1), (1, 1), (-1,-1), (-1,1)], 3, "black")
            ]
    queen = [Piece("♕", (1,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], 9),
             Piece("♛", (8,4), [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], 9, "black")
            ]
    knight = [LimitedRangePiece("♘", (1,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], 3), 
              LimitedRangePiece("♘", (1,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], 3),
              LimitedRangePiece("♞", (8,7), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], 3, "black"),
              LimitedRangePiece("♞", (8,2), [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], 3, "black")
             ]
    king = [King("♔", (1,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)], 100),
            King("♚", (8,5), [(1, 0), (-1, 0), (0, 1), (0, -1),(1, 1), (1, -1), (-1, 1), (-1, -1)], 100, "black")]

    pawns = []
    for i in range(8):
        pawns.append(Pawn("♙", (2, i+1), [(1,0)], 1))
        pawns.append(Pawn("♟", (7, i+1), [(-1,0)], 1, "black"))

    pieces: Piece = [rooks, bishop, queen, knight, king, pawns]

    return pieces

def create_label(window, row, col, text="", bg_color="#183446", fg_color="black") -> None:
    label = Label(window, text=text, bg=bg_color, fg=fg_color, font=('Helvetica 20 bold'))
    label.grid(row=row, column=col, sticky="nsew")

def create_window(cc) -> Tk:
    window = Tk()
    window.title("PyChess")
    window.resizable(False,False)

    banner_frame = CustomBanner(window, "#022F40")
    
    board_frame = Frame(window, bg="#183446")
    board_frame.pack(fill="x")

    for i in range(9):
        board_frame.grid_rowconfigure(i, weight=1, uniform="equal")
        board_frame.grid_columnconfigure(i, weight=1, uniform="equal")

    for i in range(9):
        for j in range(9):
            if i == 8 and j < 8:  # Bottom row (numbers)
                create_label(board_frame, i, j + 1, text=f"{j + 1}") #chr(65 + j)
            elif j == 0 and i < 8:  # Left column (numbers)
                create_label(board_frame, i, j, text=f"{8 - i}")

    for position, piece in Chessboard.chessboard.items():
        CustomButton(piece, cc, banner_frame, board_frame, position)

    return window

pieces: Piece = fill_figures()
cc = Chessboard(pieces)
window = create_window(cc)

print(cc)

for piece in pieces[5]:
    piece.window = window

window.mainloop()