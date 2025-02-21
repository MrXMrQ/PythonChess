from Pieces.piece import Piece

class Chessboard:
    turn: int = 0
    chessboard: dict = None

    def __init__(self, pieces: list) -> None:
        self._pieces = pieces

        Chessboard.chessboard = self.create_chessboard(pieces)

    def create_chessboard(self, pieces: Piece) -> dict:
        board = {}

        for i in range(8):
            for j in range(8):
                board.update({(8 - i, j + 1): None}) 
        
        return self.assign_chesspieces(board, pieces)

    def assign_chesspieces(self, board: dict, pieces: Piece) -> dict:
        for liste in pieces:
            for piece in liste:
                start_field: tuple = piece.start_field

                if start_field in board:
                    board[start_field] = piece

        return board

    def __str__(self) -> str:
        board = ""

        for y in range(8, 0, -1):
            for x in range(1, 9):
                piece = self.chessboard.get((y, x), ".")
                board += f"{piece.name if piece is not None else "."} "
            board += "\n"

        return board