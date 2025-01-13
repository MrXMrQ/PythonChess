from Pieces.MyPiece import Piece

class Knight(Piece):
    def __init__(self, *args):
        super().__init__(*args)

    def calculate_valid_moves(self, chessboard: dict) -> list:
        valid_moves = []
        knight_moves = [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2), (-1, 2),(-1, -2)]

        row, col = self.current_field  

        for move in knight_moves:
            new_row = row + move[0]
            new_col = col + move[1]
            next_field = (new_row, new_col)

            if next_field in chessboard:
                
                if chessboard[next_field] is None or not chessboard[next_field].is_Friend:
                    valid_moves.append(next_field)

        return valid_moves
    
    def execute_valid_move(self, field: tuple, chessboard: dict) -> None:
        if field in chessboard:
            chessboard[self.current_field] = None
            self.current_field = field
            chessboard[field] = self

        return chessboard