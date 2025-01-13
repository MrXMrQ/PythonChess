from Pieces.MyPiece import Piece

class King(Piece):
    def __init__(self, *args, is_in_chess=False):
        super().__init__(*args)
        self._is_in_chess = is_in_chess

    def calculate_valid_moves(self, chessboard: dict) -> list:
        valid_moves = []
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),  # Horizontal und Vertikal
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Diagonal
        ]  # Mögliche Bewegungsrichtungen (ein Feld in jede Richtung)

        row, col = self.current_field  # Die aktuelle Position des Königs

        # Überprüfe jede Richtung und füge das benachbarte Feld zur Liste der gültigen Züge hinzu
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            next_field = (new_row, new_col)

            # Überprüfe, ob das nächste Feld auf dem Schachbrett existiert
            if next_field in chessboard:
                # Überprüfe, ob das nächste Feld entweder leer ist oder ein gegnerisches Stück enthält
                if chessboard[next_field] is None or not chessboard[next_field].is_Friend:
                    valid_moves.append(next_field)

        return valid_moves


    def execute_valid_move(self, field: tuple, chessboard: dict) -> None:
        if field in chessboard:
            chessboard[self.current_field] = None
            self.current_field = field
            chessboard[field] = self

        return chessboard
    
    @property
    def is_in_chess(self) -> bool:
        return self._is_in_chess
    
    @is_in_chess.setter
    def is_in_chess(self, is_in_chess) -> None:
        self._is_in_chess = is_in_chess