from Pieces.MyPiece import Piece

class Queen(Piece):
    def __init__(self, name, start_field, is_Friend = True):
        super().__init__(name, start_field, is_Friend)

    def calculate_valid_moves(self, chessboard: dict) -> list:
        valid_moves = []
        directions: list = [(0, -1), (0, 1), (-1,0), (1,0), (1,1), (-1,-1), (-1,1), (1,-1)]

        for direction in directions:
            row, col = self.current_field

            while True:
                row += direction[0]
                col += direction[1]
                next_field = (row, col)

                if next_field not in chessboard:
                    break

                if chessboard[next_field] is not None:
                    if not chessboard[next_field].is_Friend:
                        valid_moves.append(next_field)
                    break
                
                valid_moves.append(next_field)

        return valid_moves
    
    def execute_valid_move(self, field: tuple, chessboard: dict) -> None:
        if field in chessboard:
            chessboard[self.current_field] = None
            self.current_field = field
            chessboard[field] = self

        return chessboard