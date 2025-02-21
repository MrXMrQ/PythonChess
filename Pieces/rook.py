from dataclasses import field
from queue import Empty
from Pieces import king
from Pieces.piece import Piece
from Pieces.king import King

from typing import override

from GUI.custom_banner import CustomBanner

class Rook(Piece):
    def __init__(self, *args, **kwargs) -> None:
        self._can_castle = True

        super().__init__(*args, **kwargs)

    @override
    def apply_move(self, king_field: tuple, chessboard: dict, banner: CustomBanner) -> dict:
        if isinstance (chessboard[king_field], King) and self._can_castle:
            self._can_castle = False
            self._moved = True,
            chessboard[king_field]._moved = True

            if self._current_field[1] > king_field[1]:
                new_rook_field = (king_field[0], king_field[1] + 1)
                new_king_field = (self._current_field[0], self._current_field[1] - 1)

            elif self._current_field[1] < king_field[1]:
                new_rook_field = (king_field[0], king_field[1] - 1)
                new_king_field = (self._current_field[0], self._current_field[1] + 2)

            chessboard[new_rook_field], chessboard[new_king_field] = chessboard[self._current_field], chessboard[king_field]

            self._current_field = new_rook_field

            if chessboard[new_king_field]:
                chessboard[new_king_field]._current_field = new_king_field

            chessboard[(self._current_field[0], 8 if king_field[1] < self._current_field[1] else 1)] = None
            chessboard[(king_field[0], 5)] = None

            return {0: chessboard, 1: new_king_field, 2: new_rook_field}
        
        return super().apply_move(king_field, chessboard, banner)
    
    def castle(self, chessboard: dict) -> tuple:
        specific_fields = self.field_between_rook_and_king(chessboard, [])
    
        if not len(specific_fields) == 0 and self.all_keys_None(specific_fields, chessboard):
            for i in chessboard:
                if isinstance(chessboard[i], King) and chessboard[i]._team == self._team and not (self._moved or chessboard[i]._moved):
                    return chessboard[i]._current_field

        return None
    
    def field_between_rook_and_king(self, chessboard: dict, specific_fields: list) -> list:
        fields = []
        king_field = None

        for i in chessboard:
            if i[0] == self._current_field[0]:
                if isinstance(chessboard[i], King):
                    king_field = i
                fields.append(i)

        if king_field is None:
            return []

        if self._current_field[1] < king_field[1]:
            specific_fields = [field for field in fields if field[1] < king_field[1] and field[1] > self._current_field[1]]
        elif self._current_field[1] > king_field[1]:
            specific_fields = [field for field in fields if field[1] > king_field[1] and field[1] < self._current_field[1]]

        return specific_fields
    
    def all_keys_None(self, keys: list, data_dict: dict) -> bool:
        return all(data_dict[key] is None for key in keys)

    @property
    def can_castle(self) -> bool:
        return self._can_castle