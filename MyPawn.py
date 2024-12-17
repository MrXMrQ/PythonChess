from MyFigure import Figure

class Pawn(Figure):
    """
    Represents a pawn in a chess game.

    Inherits:
        Figure: Base class for game figures like pawn, rook...

    Attributes:
        first_move (bool): Indicates if the pawn has made its first move.
        is_at_end (bool): Indicates if the pawn has reached the end of the board.
    """

    def __init__(self, name: str, start_field: tuple, is_Friend: bool = True, first_move: bool = True, is_at_end: bool = False) -> None:
        """
        Initialize a Pawn instance.

        Args:
            name (str): The name of the pawn.
            start_field (tuple): The starting field of the pawn as (x, y).
            is_Friend (bool, optional): Indicates if the pawn is a friendly piece. Defaults to True.
            first_move (bool, optional): Indicates if the pawn is on its first move. Defaults to True.
            is_at_end (bool, optional): Indicates if the pawn has reached the end of the board. Defaults to False.
        """

        super().__init__(name, start_field, is_Friend)
        self.first_move = first_move
        self.is_at_end = is_at_end

    def calculate_valid_moves(self, chessboard: dict) -> list:
        """
        Calculate the list of valid moves for a pawn based on its current position.

        The valid moves for a pawn are determined based on its current position and 
        whether it is its first move or not. For a pawn, valid moves involve moving 
        one square forward or two squares forward from its starting position. 
        This method checks all possible squares for a valid move based on the row and 
        column conditions and appends valid ones to the result list.

        Args:
            chessboard (dict): A dictionary representing the chessboard with keys as positions (tuples) and values as pieces on the board.

        Returns:
            list: A list of valid move positions for the pawn.
        """

        valid_moves: list = []

        for i in chessboard:
            if i[1] == self.current_field[1] and (i[0] - self.current_field[0] == 1 or (i[0] - self.current_field[0] == 2 and self.first_move)):
                valid_moves.append(i)

        return valid_moves


    def execute_valid_move(self, field: tuple, chessboard: dict) -> None:
        """
        Execute a valid move for the pawn on the chessboard.

        This method updates the chessboard by moving the pawn from its current position
        to the target field. It also ensures that the pawn cannot move to an invalid 
        location (not on the board), and it updates the `first_move` attribute of the pawn.

        Args:
            field (tuple): The target position (row, column) on the chessboard.
            chessboard (dict): A dictionary representing the chessboard.

        Raises:
            IndexError: If the field is not a valid position on the chessboard.

        Returns:
            dict: The updated chessboard after the move.
        """

        if field in chessboard:
            self.first_move = False
            chessboard[self.current_field] = None
            self.current_field = field
            chessboard[field] = self
        else:
            raise IndexError("{} does not exist in dict chessboard in execute_valid_move for pawn".format(field))

        return chessboard

    def get_Field(self) -> tuple:
        """
        Get the current field of the pawn.

        Returns:
            tuple: The current field of the pawn as (x, y).
                x: hight (left_value)
                y: widht (right_value)
        """
        return self.current_field