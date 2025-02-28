from tkinter import Tk, Button, Toplevel, Label

from Pieces.knight import LimitedRangePiece
from GUI.custom_banner import CustomBanner
from Pieces.piece import Piece

from GUI.custom_button import CustomButton

from typing import override

class Pawn(Piece):
    """
    Represents a pawn piece in a chess game.

    Attributes:
        _window (Tk): The Tkinter window used for UI interactions.
        _current_field (tuple): The current position of the pawn on the board.
        _moved (bool): Indicates whether the pawn has moved before.
        _team (str): The team color ("white" or "black") of the pawn.
        _name (str): The name or symbol representing the pawn.

    Methods:
        compute_moves(chessboard: dict) -> list:
            Computes all valid moves for the pawn based on its movement rules.

        apply_move(chessboard: dict, field: tuple, banner: CustomBanner) -> dict:
            Moves the pawn to the given field and handles promotion if applicable.

        _diagonal_fields(one_step) -> list[tuple, tuple]:
            Returns the diagonal attack positions based on the pawn's current move direction.

        _open_popup(chessboard: dict, team: str, banner: CustomBanner) -> None:
            Opens a UI popup to allow the player to select a promotion piece.

        _replace(chessboard: dict, piece: Piece, banner: CustomBanner) -> None:
            Replaces the current pawn with a promoted piece.
    """

    def __init__(self, *args, **kwargs) -> None:
        self._window = None

        super().__init__(*args, **kwargs)

    @override
    def compute_moves(self, chessboard: dict) -> list:
        """
        Computes all valid moves for the pawn piece based on the current chessboard state.
            - two steps or one step on start
            - diagonal attack

        Args:
            chessboard (dict): The current state of the chessboard, mapping positions to pieces.

        Returns:
            list: A list of valid moves as tuples.

        Raises:
            TypeError: If chessboard is not a dictionary.
        """

        valid_moves = []
        row, col = self.current_field
        direction = 1 if self._team == "white" else - 1

        one_step = (row + direction, col)

        if one_step in chessboard and chessboard[one_step] is None:
            valid_moves.append(one_step)

            two_steps = (row + 2 * direction, col)
            if not self._moved and two_steps in chessboard and chessboard[two_steps] is None:
                valid_moves.append(two_steps)

        for diagonal in self._diagonal_fields():
            if diagonal in chessboard and chessboard[diagonal] is not None:
                if chessboard[diagonal]._team != self._team:
                    valid_moves.append(diagonal)   

        return valid_moves
    
    def _diagonal_fields(self) -> list[tuple, tuple]:
        field = self._current_field
        direction = 1 if self._team == "white" else - 1

        return [(field[0] + direction, field[1] - 1), (field[0] + direction, field[1] + 1)]

    @override
    def apply_move(self, chessboard: dict, field: tuple, banner: CustomBanner) -> dict:
        """
        Moves the piece to the specified field and handles pawn promotion.

        Args:
            chessboard (dict): A dictionary representing the current state of the chessboard.
            field (tuple): The target position (row, column) to move the piece to.
            banner (CustomBanner): The UI banner object used to update the game state.

        Returns:
            dict: The updated chessboard after the move.
        """

        board = super().apply_move(chessboard, field, banner)

        if self._current_field[0] in {1, 8}:
            team_color = "white" if self._current_field[0] == 8 else "black"
            self._open_popup(chessboard, team_color, banner)

        return board
    
    def _open_popup(self, chessboard: dict, team: str, banner: CustomBanner) -> None:
        """
        Opens a popup window for pawn promotion selection.

        Args:
            chessboard (dict): A dictionary representing the current state of the chessboard.
            team (str): The team color ("white" or "black") of the promoting piece.
            banner (CustomBanner): The UI banner object used to update the game state.

        Returns:
            None
        """

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

        knight = LimitedRangePiece("♘" if team == "white" else "♞", self._current_field, [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)], 3, team)
        rook = Piece("♖" if team == "white" else "♜", self._current_field, [(1, 0), (-1, 0), (0, 1), (0, -1)], 5, team)
        bishop = Piece("♗" if team == "white" else "♝", self._current_field, [(1, -1), (1, 1), (-1,-1), (-1,1)], 3, team)
        queen = Piece("♕" if team == "white" else "♛", self._current_field, [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1,-1), (-1,1)], 9, team)
        
        for piece, symbol in zip([knight, rook, bishop, queen], ["♘", "♖", "♗", "♕"] if team == "white" else ["♞", "♜", "♝", "♛"]):
            Button(popup, text=symbol, command=lambda p=piece: [self._replace(chessboard, p, banner), popup.destroy()], **btn_style).pack(pady=10)

        self._window.wait_window(popup) 

    def _replace(self, chessboard: dict, piece: Piece, banner: CustomBanner) -> None:
        """
        Replaces the current piece with a promoted piece on the chessboard.

        Args:
            chessboard (dict): A dictionary representing the current state of the chessboard.
            piece (Piece): The promoted piece to replace the current one.
            banner (CustomBanner): The UI banner object used to display game updates.

        Returns:
            None
        """

        chessboard[self._current_field] = piece
        CustomButton._button_registry[self.current_field]._content = piece
        banner.change_text(f"{self._team.capitalize()} PROMOTES {self._name} to {piece.name}", None)
        
    @property
    def window(self) -> Tk:
        return self._window
    
    @window.setter
    def window(self, other) -> None:
        if not isinstance(other, Tk):
            raise ValueError(f"ERROR: 'root' must be type tk (window) not {type(other)}")
        
        self._window = other