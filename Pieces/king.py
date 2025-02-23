from Pieces.limited_range_piece import LimitedRangePiece
from Pieces.piece import Piece

from typing import override

def get_pawn():
    from Pieces.pawn import Pawn  # Import erst bei Funktionsaufruf
    return Pawn

class King(LimitedRangePiece):
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
                if self._team == "white":
                    if chessboard[next_field] is None or not chessboard[next_field]._team == "white":
                        valid_moves.append(next_field)
                elif self._team == "black":
                    if chessboard[next_field] is None or not chessboard[next_field]._team == "black":
                        valid_moves.append(next_field)
                else:
                    raise ValueError(f"ERROR: object have no team: {self._team}")
                
        other_moves = []
                
        for i in chessboard:
            piece: Piece = chessboard[i]
            if piece is not None and piece.team != self._team:
                
                if isinstance(piece, get_pawn()):
                    other_moves += piece.diagonal_fields()
                    continue

                if isinstance(piece, King):
                    other_moves += self.get_sorunding_fields(chessboard, piece)
                    continue
                
                other_moves += piece.compute_moves(chessboard)  

        other_moves.sort()

        for i in other_moves:
            if i in valid_moves:
                valid_moves.remove(i)  

        return valid_moves
    
    def get_sorunding_fields(self, chessboard: dict, enemy_king: Piece) -> list:
        x, y = enemy_king._current_field
        fields = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]

        for field in fields:
            if field not in chessboard:
                fields.remove(field)

        return fields

    def check(self) -> None:
        pass

    def check_mate(self) -> None:
        pass