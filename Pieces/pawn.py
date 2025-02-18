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
        return super().__str__() + f", {self._team}"

    @override
    def compute_moves(self, chessboard: dict) -> list:
        valid_moves = []
        row, col = self.current_field
        print(row, col)

        if self._team == "white":
            one_step = (row + 1, col)
        elif self._team == "black":
            one_step = (row - 1, col)
        else:
            raise ValueError(f"ERROR: object have no team: {self._team}")

        if one_step in chessboard and chessboard[one_step] is None:
            valid_moves.append(one_step)

            if self._team == "white":
                two_steps = (row + 2, col)
            elif self._team == "black":
                two_steps = (row - 2, col)
            else:
                raise ValueError(f"ERROR: object have no team: {self._team}")

            if not self._first_move and two_steps in chessboard and chessboard[two_steps] is None:
                valid_moves.append(two_steps)

        if self._team == "white":
            diagonal_left = (row + 1, col - 1)
            diagonal_right = (row + 1, col + 1)
        elif self._team == "black":
            diagonal_left = (row - 1, col - 1)
            diagonal_right = (row - 1, col + 1)
        else:
            raise ValueError(f"ERROR: object have no team: {self._team}")

        if diagonal_left in chessboard and chessboard[diagonal_left] is not None:
            if self._team == "white":
                if not chessboard[diagonal_left]._team == "white":
                    valid_moves.append(diagonal_left)
            elif self._team == "black":
                if not chessboard[diagonal_left]._team == "black":
                    valid_moves.append(diagonal_left)
            else:
                raise ValueError(f"ERROR: object have no team: {self._team}")

        if diagonal_right in chessboard and chessboard[diagonal_right] is not None:
            if self._team == "white":
                if not chessboard[diagonal_right]._team == "white":
                    valid_moves.append(diagonal_right)
            elif self._team == "black":
                if not chessboard[diagonal_right]._team == "black":
                    valid_moves.append(diagonal_right)
            else:
                raise ValueError(f"ERROR: object have no team: {self._team}")
        
        return valid_moves
    
    @override
    def apply_move(self, field: tuple, chessboard: dict) -> None:
        self._first_move = True

        board = super().apply_move(field, chessboard)

        if self._current_field[0] == 8:
            self.open_popup(chessboard, "white")
        elif self._current_field[0] == 1:
            self.open_popup(chessboard, "black")

        return board
    
    def open_popup(self, chessboard: dict, team: str) -> None:
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

        knight = LimitedRangePiece("♘" if team == "white" else "♞", self._current_field, [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], team)
        rook = Piece("♖" if team == "white" else "♜", self._current_field, [(1, 0), (-1, 0), (0, 1), (0, -1)], team)
        bishop = Piece("♗" if team == "white" else "♝", self._current_field, [(1, -1), (1, 1), (-1,-1), (-1,1)], team)
        queen = Piece("♕" if team == "white" else "♛", self._current_field, [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], team)
        
        Button(popup, text="♘" if team == "white" else "♞", command=lambda: [self.replace(knight, chessboard), popup.destroy()], **btn_style).pack(pady=10)
        Button(popup, text="♖" if team == "white" else "♜", command=lambda: [self.replace(rook, chessboard), popup.destroy()], **btn_style).pack(pady=10)
        Button(popup, text="♗" if team == "white" else "♝", command=lambda: [self.replace(bishop, chessboard), popup.destroy()], **btn_style).pack(pady=10)
        Button(popup, text="♕" if team == "white" else "♛", command=lambda: [self.replace(queen, chessboard), popup.destroy()], **btn_style).pack(pady=10)

        self._window.wait_window(popup) 

    def replace(self, piece: Piece, chessboard: dict) -> None:
        chessboard[self._current_field] = piece
    
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