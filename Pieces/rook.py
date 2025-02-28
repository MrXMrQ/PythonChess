from Pieces.piece import Piece
from Pieces.king import King

from GUI.custom_banner import CustomBanner

from typing import override

class Rook(Piece):
    """
    Represents a rook in a chess game, including its movement and castling behavior.

    Attributes:
        _can_castle (bool): Indicates whether the rook is still eligible for castling.

    Methods:
        apply_move(chessboard, king_position, banner):
            Executes a move, including castling if conditions are met.
        
        castle(chessboard):
            Determines if castling is possible and returns the king's position if valid.
        
        _field_between_rook_and_king(chessboard):
            Identifies the squares between the rook and the king on the same rank.
        
        _all_keys_None(keys, data_dict):
            Checks if all specified keys in a dictionary have None values.
    """

    def __init__(self, *args, **kwargs) -> None:
        self._can_castle = True

        super().__init__(*args, **kwargs)

    @override
    def apply_move(self, chessboard: dict, king_position: tuple, banner: CustomBanner) -> dict:
        """
        Executes a castling move if possible; otherwise, applies a standard move.

        Args:
            king_position (tuple): The target position of the king.
            chessboard (dict): The current chessboard state.
            banner (CustomBanner): The banner used to update the score if a piece is captured.

        Returns:
            dict: A dictionary containing the updated chessboard and new positions.
        """
        
        if isinstance (chessboard[king_position], King) and self._can_castle:
            self._can_castle = False
            self._moved = True,
            chessboard[king_position]._moved = True

            rook_y, rook_x = self._current_field
            king_y, king_x = king_position

            if rook_x > king_x:  # Queenside castling (long castling)
                new_rook_position = (king_y, king_x + 1)
                new_king_position = (rook_y, rook_x - 1)
            else:  # Kingside castling (short castling)
                new_rook_position = (king_y, king_x - 1)
                new_king_position = (rook_y, rook_x + 2)

            chessboard[new_rook_position], chessboard[new_king_position] = chessboard[self._current_field], chessboard[king_position]
            self._current_field = new_rook_position
            chessboard[new_king_position]._current_field = new_king_position

            chessboard[(rook_y, 8 if king_x < rook_x else 1)] = None
            chessboard[(rook_y, 5)] = None

            return [chessboard, new_king_position, new_rook_position]
        
        return super().apply_move(chessboard, king_position, banner)
    
    def castle(self, chessboard: dict) -> tuple:
        """
        Determines if castling is possible and returns the king's position if valid.

        Castling is possible if:
        - There are no pieces between the king and the rook.
        - Neither the king nor the rook has moved before.
        - The king is not in check, nor does it pass through or end in check.

        Args:
            chessboard (dict): The current state of the chessboard, mapping positions to pieces.

        Returns:
            tuple | None: The king's position if castling is possible, otherwise None.
        """
        
        specific_fields = self._field_between_rook_and_king(chessboard)
    
        if specific_fields and self._all_keys_None(specific_fields, chessboard):
            for position, piece in chessboard.items():
                if isinstance(piece, King) and piece._team == self._team and not (self._moved or piece._moved):
                    return piece._current_field

        return None
    
    def _field_between_rook_and_king(self, chessboard: dict) -> list:
        """
        Identifies the squares between the rook and the king on the same rank.

        Args:
            chessboard (dict): The current state of the chessboard.

        Returns:
            list: A list of board positions (tuples) between the rook and the king.
        """

        king_field = next((pos for pos, piece in chessboard.items() if isinstance(piece, King) and pos[0] == self._current_field[0]), None)

        if king_field is None:
            return []

        return [
            field for field in chessboard
            if  (self._current_field[1] < king_field[1] > field[1]) and field[0] == self._current_field[0] and field != self._current_field or 
                (self._current_field[1] > king_field[1] < field[1]) and field[0] == self._current_field[0] and field != self._current_field
        ]
    
    def _all_keys_None(self, keys: list, data_dict: dict) -> bool:
        """
        Checks if all given keys in a dictionary have None values.

        Args:
            keys (list): A list of dictionary keys to check.
            data_dict (dict): The dictionary containing key-value pairs.

        Returns:
            bool: True if all specified keys map to None, otherwise False.
        """

        for key in keys:
            if key not in data_dict:
                raise KeyError(f"Key: {key} not in data dict: {data_dict}")

        return all(data_dict[key] is None for key in keys)

    @property
    def can_castle(self) -> bool:
        return self._can_castle