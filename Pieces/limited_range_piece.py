from typing import override
from Pieces.piece import Piece


class LimitedRangePiece(Piece):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @override
    def compute_moves(self, chessboard) -> list:
        valid_moves = []
        directions = self.directions
        
        row, col = self.current_field

        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            next_field = (new_row, new_col)

            if next_field in chessboard:
                if chessboard[next_field] is None or not chessboard[next_field].is_friend:
                    valid_moves.append(next_field)

        return valid_moves