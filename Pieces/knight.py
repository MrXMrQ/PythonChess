from Pieces.piece import Piece

from typing import override

class Knight(Piece):
    """
    Represents a chess piece with a limited movement range.
    
    This class extends the `Piece` class and allows movement only 
    within predefined directional limits.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @override
    def compute_moves(self, chessboard, append_protected_field = False) -> list:
        """
        Computes all valid moves for the knight piece.

        Args:
            chessboard (dict): The current chessboard state.

        Returns:
            list: A list of valid move positions as (row, col) tuples.
        """

        valid_moves = []
        row, col = self.current_field

        for drY, drX in self._directions:
            next_field = (row + drY, col + drX)

            if next_field in chessboard:
                piece_at_field = chessboard[next_field]

                if piece_at_field is None or piece_at_field._team != self._team:
                    valid_moves.append(next_field)

                if append_protected_field and piece_at_field and piece_at_field._team == self._team:
                    Piece.protected_fields.append(next_field)
                    
        return valid_moves