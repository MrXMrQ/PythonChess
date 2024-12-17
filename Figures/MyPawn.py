from Figures.MyFigure import Figure

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
        Calculates all valid trains for a pawn. 
        - A pawn moves up (negative direction in lines). 
        - The pawn can take two steps at the starting field. 
        - The pawn can strike diagonally if there is an opposing figure there. 
        
        Args: 
            chessboard (dict): The chessboard as a dictionary. 
        Returns: 
            list: A list of valid trains for the farmer.
        """
        valid_moves = []
        row, col = self.current_field
    
        one_step = (row + 1, col)
        if one_step in chessboard and chessboard[one_step] is None:
            valid_moves.append(one_step)

            two_steps = (row + 2, col)
            if self.first_move and two_steps in chessboard and chessboard[two_steps] is None:
                valid_moves.append(two_steps)

        diagonal_left = (row + 1, col - 1)
        diagonal_right = (row + 1, col + 1)

        if diagonal_left in chessboard and chessboard[diagonal_left] is not None:
            if not chessboard[diagonal_left].is_Friend:
                valid_moves.append(diagonal_left)

        if diagonal_right in chessboard and chessboard[diagonal_right] is not None:
            if not chessboard[diagonal_right].is_Friend:
                valid_moves.append(diagonal_right)

        return valid_moves

    def execute_valid_move(self, field: tuple, chessboard: dict) -> dict:
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