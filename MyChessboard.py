from MyFigure import Figure
from MyCustomButton import Custom_Button
from tkinter import *

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
            board.update({(8 - i, j + 1): None}) 
        
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
                board[start_field] = piece

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

    from tkinter import Tk, Label

    def create_label(self, window, row, col, text="", bg_color="white", fg_color="black"):
        """
        Creates and places a label in the given window at the specified grid position.

        Args:
            window (Tk): The parent Tkinter window.
            row (int): The row in the grid where the label will be placed.
            col (int): The column in the grid where the label will be placed.
            text (str, optional): The text to display in the label. Defaults to an empty string.
            bg_color (str, optional): Background color of the label. Defaults to "white".
            fg_color (str, optional): Foreground color (text color) of the label. Defaults to "black".
        """
        label = Label(window, text=text, bg=bg_color, fg=fg_color)
        label.grid(row=row, column=col, sticky="nsew")

    def create_window(self) -> Tk:
        """
        Creates the chessboard window, configures the grid, and populates it with labels and buttons.

        The window includes:
            - A chessboard grid with row and column labels.
            - A dynamic chessboard where pieces are represented as buttons.

        Returns:
            Tk: The created Tkinter window.
        """
        window = Tk()
        window.title("Chessboard")
        window.minsize(500, 500)

        # Configure the grid layout to make rows and columns expandable
        for i in range(9):
            window.grid_rowconfigure(i, weight=1)
            window.grid_columnconfigure(i, weight=1)

        # Add row and column labels (numbers) for the chessboard
        for i in range(9):
            for j in range(9):
                if i == 8 and j < 8:  # Bottom row (numbers)
                    self.create_label(window, i, j + 1, text=f"{j + 1}")
                elif j == 0 and i < 8:  # Left column (numbers)
                    self.create_label(window, i, j, text=f"{8 - i}")

        # Add the chessboard pieces as buttons (Custom_Button is assumed to be defined elsewhere)
        for position, piece in self.board.items():
            row, col = position
            text = f"{row} {col} "
        
            if piece is not None:
                text = piece.name  # Use the piece's name for display
        
            # Set the color for the button based on the position
            button_color = "lightgray" if (row + col) % 2 == 0 else "gray"
            Custom_Button(window, text, button_color, position, self.board)

        return window


    def update_chessboard(self, window, old_value, new_value):
        """
        Updates the chessboard by moving a piece from one position to another.

        Args:
            old_value: The current position of the piece to be moved.
            new_value: The new position to move the piece to.

        Returns:
            None
        """
        
        pass

    def get_board_dict(self) -> dict:
        return self.board