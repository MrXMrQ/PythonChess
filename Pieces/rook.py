from Pieces.piece import Piece
from Pieces.king import King

from typing import override

class Rook(Piece):
    def __init__(self, *args, **kwargs) -> None:
        self._can_castle = True

        super().__init__(*args, **kwargs)

    @override
    def apply_move(self, field, chessboard) -> None:
        if field == (self._current_field[0], self._current_field[1] - 3) and self._can_castle:
            self._can_castle = False

            rook_pos = self._current_field
            king_pos = (rook_pos[0], rook_pos[1] - 3)

            king_castle_pos = (rook_pos[0], rook_pos[1] - 1)
            rook_castle_pos = (rook_pos[0], rook_pos[1] - 2)

            chessboard[king_castle_pos] = chessboard[king_pos]
            #chessboard[king_castle_pos].current_field = king_castle_pos
            chessboard[king_pos] = None

            chessboard[rook_castle_pos] = chessboard[rook_pos]
            #chessboard[rook_castle_pos].current_field = rook_castle_pos
            chessboard[rook_pos] = None

            return chessboard

        return super().apply_move(field, chessboard)

    def castle(self, chessboard: dict) -> tuple:
        for i in chessboard:
            if isinstance(chessboard[i], King) and chessboard[i]._team == self._team and not (self._moved or chessboard[i]._moved):
                bishop_field = chessboard[self._current_field[0], self._current_field[1] - 2]
                knight_field = chessboard[self._current_field[0], self._current_field[1] - 1]

                if bishop_field is None and knight_field is None:
                    return chessboard[i]._current_field
                
        return None
    
    @property
    def can_castle(self) -> bool:
        return self._can_castle