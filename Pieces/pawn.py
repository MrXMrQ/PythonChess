from math import pi
from typing import override
from tkinter import *
from Pieces.piece import Piece
from Pieces.limited_range_piece import LimitedRangePiece

class Pawn(Piece):
    def __init__(self, *args, **kwargs) -> None:
        self._first_move = False
        self._window = None

        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return super().__str__() + f", {self._is_friend}"
    
    def replace(self, piece: Piece, chessboard: dict) -> None:
        chessboard[self._current_field] = piece
    
    def open_popup(self, chessboard: dict) -> None:
        popup = Toplevel(self._window)
        popup.geometry("400x400")
        popup.title("Promotion Selection")
        popup.resizable(False, False)
    
        popup.transient(self._window)  
        popup.grab_set()    
        popup.protocol("WM_DELETE_WINDOW", lambda: None)

        
        popup.grid_rowconfigure(3,weight=1)
        popup.grid_columnconfigure(2,weight=1)

        Label(master=popup, text="Choose your promotion piece", font=('Helvetica 14 bold')).pack(pady=10)

        btn_style = {"font": ('Helvetica', 22, 'bold'), "padx": 5, "pady": 5}

        knight = LimitedRangePiece("♘", self._current_field, [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)])
        rook = Piece("♖", self._current_field, [(1, 0), (-1, 0), (0, 1), (0, -1)])
        bishop = Piece("♗", self._current_field, [(1, -1), (1, 1), (-1,-1), (-1,1)])
        queen = Piece("♕", self._current_field, [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)])
        
        Button(popup, text="♘", command=lambda: [self.replace(knight, chessboard), popup.destroy()], **btn_style).pack(pady=10)
        Button(popup, text="♖", command=lambda: [self.replace(rook, chessboard), popup.destroy()], **btn_style).pack(pady=10)
        Button(popup, text="♗", command=lambda: [self.replace(bishop, chessboard), popup.destroy()], **btn_style).pack(pady=10)
        Button(popup, text="♕", command=lambda: [self.replace(queen, chessboard), popup.destroy()], **btn_style).pack(pady=10)

        self._window.wait_window(popup) 

    @override
    def compute_moves(self, chessboard: dict) -> list:
        valid_moves = []
        row, col = self.current_field
    
        one_step = (row + 1, col)
        if one_step in chessboard and chessboard[one_step] is None:
            valid_moves.append(one_step)

            two_steps = (row + 2, col)
            if not self._first_move and two_steps in chessboard and chessboard[two_steps] is None:
                valid_moves.append(two_steps)

        diagonal_left = (row + 1, col - 1)
        diagonal_right = (row + 1, col + 1)

        if diagonal_left in chessboard and chessboard[diagonal_left] is not None:
            if not chessboard[diagonal_left].is_friend:
                valid_moves.append(diagonal_left)

        if diagonal_right in chessboard and chessboard[diagonal_right] is not None:
            if not chessboard[diagonal_right].is_friend:
                valid_moves.append(diagonal_right)

        return valid_moves
    
    @override
    def apply_move(self, field: tuple, chessboard: dict) -> None:
        self._first_move = True

        board = super().apply_move(field, chessboard)

        if self.current_field[0] == 8:
            self.open_popup(chessboard)

        return board
    
    @property
    def first_move(self) -> bool:
        return self._first_move
    
    @first_move.setter
    def first_move(self, other) -> None:
        if not isinstance(other, bool):
            raise ValueError(f"ERROR: 'first_move' must be type 'bool' not type {type(other)}")
        
    @property
    def window(self) -> Tk:
        return self._window
    
    @window.setter
    def window(self, other) -> None:
        if not isinstance(other, Tk):
            raise ValueError(f"ERROR: 'root' must be type tk (window) not {type(other)}")
        
        self._window = other