from MyFigure import Figure

def check_statement(old_x: int, new_x: int, old_y: int, new_y: int) -> bool:
        """
        Check if the movement of a pawn is valid.

        A valid movement is one where the x-coordinate remains the same, the y-coordinate
        increases by exactly 1, and the movement direction is forward.

        Args:
            old_x (int): The original x-coordinate of the pawn.
            new_x (int): The new x-coordinate of the pawn.
            old_y (int): The original y-coordinate of the pawn.
            new_y (int): The new y-coordinate of the pawn.

        Returns:
            bool: True if the move satisfies the conditions, otherwise False.
        """
        return old_x == new_x and new_y > old_y and new_y - old_y == 1

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

    def move(self, potential_new_field: tuple):
        """
        Attempt to move the pawn to a new field.

        If the move is valid, update the pawn's position. The first move allows for an optional two-square movement.
        If the pawn reaches the end of the board, mark it as such.

        Args:
            potential_new_field (tuple): The target field as (x, y) to which the pawn intends to move.

        Returns:
            None
        """

        old_x, old_y, new_x, new_y = self.current_field[0], self.current_field[1], potential_new_field[0], potential_new_field[1], 

        # If the pawn is at the end, no more movement is accepted!
        if self.is_at_end:
            return

        # new_y - old_y == 2 and self.first_move: to check if the pawn can move two squares forward, but only on its first move.
        if  check_statement(old_x, new_x, old_y, new_y) or (new_y - old_y == 2 and self.first_move):
            self.first_move = False
            self.current_field = potential_new_field

            if self.current_field[1] == 8:
                self.is_at_end = True
            
        else:
            pass

    def get_Field(self) -> tuple:
        """
        Get the current field of the pawn.

        Returns:
            tuple: The current field of the pawn as (x, y).
        """
        return self.current_field
    
    def kill_instance(self) -> None:
        """
        Handle the pawn being removed from the game.

        Returns:
            None
        """
        pass