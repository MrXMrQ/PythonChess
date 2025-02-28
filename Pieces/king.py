from Pieces.piece import Piece

from typing import override

def get_pawn():
    """
    Dynamically loads the Pawn class to avoid circular imports.
    """

    from Pieces.pawn import Pawn
    return Pawn

class King(Piece):
    """
    Represents the King piece in chess.

    Attributes:
        current_field (tuple): The King's current position on the board.
        _team (str): The color of the King ("white" or "black").
        _directions (list): A list of all possible movement directions.

    Methodes:
        compute_moves(self, chessboard) -> list:   
            Computes all valid moves for the king piece while considering other pieces potential threats.

        _get_surrounding_fields(self, chessboard: dict, enemy_king: Piece) -> list:
            return a list from the surrounding fields of the enemy king
    """
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @override
    def compute_moves(self, chessboard, append_protected_field = False) -> list:
        """
        Computes all valid moves for the king piece while considering other pieces potential threats.

        Args:
            chessboard (dict): The current chessboard state, mapping positions to pieces.

        Returns:
            list: A list of valid moves that are not under threat.
        """

        valid_moves = [] 
        row, col = self.current_field

        print(f"Protected field: {Piece.protected_fields}")

        for drY, drX in self._directions:
            next_field = (row + drY, col + drX)

            if next_field in chessboard:
                piece_at_field = chessboard[next_field]
                if piece_at_field is None or piece_at_field.team != self._team and next_field not in Piece.protected_fields:
                    valid_moves.append(next_field)    
                
                if append_protected_field and piece_at_field and piece_at_field._team == self._team:
                    Piece.protected_fields.append(next_field)
        
        threatened_moves = self.get_threatened_moves(chessboard)

        return [move for move in valid_moves if move not in threatened_moves]
    
    def get_threatened_moves(self, chessboard: dict) -> list:
        threatened_moves = []

        for position, piece_at_field in chessboard.items():
            if piece_at_field and piece_at_field.team != self._team:
                if isinstance(piece_at_field, get_pawn()):
                    threatened_moves += piece_at_field._diagonal_fields()
                elif isinstance(piece_at_field, King):
                    threatened_moves += self._get_surrounding_fields(chessboard, piece_at_field)   
                else:
                    threatened_moves += piece_at_field.compute_moves(chessboard)

        return threatened_moves

    def _get_surrounding_fields(self, chessboard: dict, enemy_king: Piece) -> list:
        """
        Returns all surrounding fields of the given enemy king that are on the chessboard.

        Args:
            chessboard (dict): The current state of the chessboard.
            enemy_king (Piece): The enemy king whose surrounding fields are to be checked.

        Returns:
            list: A list of valid surrounding fields as tuples.
        """

        x, y = enemy_king._current_field
        fields = [
            (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), 
            (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)
        ]

        return [field for field in fields if field in chessboard]