from Pieces.piece import Piece

from typing import override

class LimitedRangePiece(Piece):
    """
    Represents a chess piece with a limited movement range.
    
    This class extends the `Piece` class and allows movement only 
    within predefined directional limits.
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @override
    def compute_moves(self, chessboard) -> list:
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
                piece_at_target = chessboard[next_field]

                if piece_at_target is None or piece_at_target._team != self._team:
                    valid_moves.append(next_field)
                    
        return valid_moves