from MyFigure import Figure

class Rook(Figure):
    def __init__(self, name: str, start_field: tuple, is_Friend: bool = True):
        super().__init__(name, start_field, is_Friend)

    def calculate_valid_moves(self, chessboard: dict) -> list:
        """
        Calculates all valid trains for the tower. The tower can only be along the Move rows (horizontal) and columns (vertical), but is blocked by figures. 
        
        Args: 
            chessboard (dict): The chessboard as a dictionary that has positions as a key. 
        
        Returns: 
            list: A list of valid trains for the tower. 
        """
        valid_moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Move direction: up, down, right, left

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