from MyFigure import Figure

def create_chessboard(pieces: Figure) -> dict:
    """
    Creates an initial chessboard representation as a dictionary.

    The chessboard is represented as an 8x8 grid where each key is a tuple
    corresponding to a position (column, row), and the value is a tuple containing
    the position and the chess piece (or None if the square is empty).

    Args:
        pieces (Figure): A Figure object containing the chess pieces to place on the board.

    Returns:
        dict: A dictionary representing the initialized chessboard with pieces assigned.
    """

    board = {}

    for i in range(8):
        for j in range(8):
            board.update([((j + 1, i + 1), ((j + 1, i + 1), None))]) 
        
    return assign_chesspieces(board, pieces)

def assign_chesspieces(board: dict, pieces: Figure) -> dict:
    """
    Assigns chess pieces to their starting positions on the board.

    Updates the board dictionary with the positions of the chess pieces
    based on their starting positions.

    Args:
        board (dict): The chessboard dictionary to update.
        pieces (Figure): A Figure object containing the chess pieces to place.

    Returns:
        dict: The updated chessboard dictionary with pieces assigned.
    """

    for piece_group in range(len(pieces)):
        for piece in pieces[piece_group]:
            start_field: tuple = piece.start_field
            if start_field in board:
                board[start_field] = (start_field, piece)

    return board

class Chessboard:
    """
    Represents a chessboard with pieces and provides methods to interact with it.

    Attributes:
        pieces (list): A list of chess pieces on the board.
        board (dict): A dictionary representing the current state of the chessboard.
    """

    def __init__(self, pieces: list):
        """
        Initializes the Chessboard with a list of pieces and sets up the board.

        Args:
            pieces (list): A list of chess pieces to place on the board.
        """

        self.pieces = pieces
        self.board = create_chessboard(pieces)

    def print_formated_chessboard(self) -> None:
        """
        Print a chessboard representation based on the given dictionary.

        Args:
            board (dict): A dictionary where keys represent board positions
                      and values are lists containing piece information.
        """
        for index, key in enumerate(self.board, start=1):
            print(self.board[key][0], end="")

            if not self.board[key][1] == None:
                print(self.board[key][1].name, end="")

            # Add a newline after every 8 elements (end of a row)
            if index % 8 == 0:
                print()
    
    def update_chessboard(self, old_value, new_value):
        """
        Updates the chessboard by moving a piece from one position to another.

        Args:
            old_value: The current position of the piece to be moved.
            new_value: The new position to move the piece to.

        Returns:
            None
        """
        
        pass