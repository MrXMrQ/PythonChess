from tkinter import *

class Custom_Button(Button):
    """
    A custom button class for a chessboard interface in Tkinter.

    Attributes:
        all_buttons (dict): A dictionary mapping positions (tuples) to button instances.
        last_move_buttons (list): A list of buttons representing the last highlighted valid moves.
        last_button (Custom_Button): The last button clicked, used for tracking state.
    """
    all_buttons: dict = {}
    last_move_buttons: list = []
    last_button = None

    def __init__(self, window, text: str, bg_color: str, k_value: tuple, chessboard: dict, is_pressed: bool = False):
        """
        Initializes a Custom_Button instance.

        Args:
            window: The parent Tkinter window.
            text (str): The text to display on the button.
            bg_color (str): The background color of the button.
            k_value (tuple): The position (row, column) of the button on the chessboard.
            chessboard (dict): The current state of the chessboard as a dictionary.
            is_pressed (bool): Indicates if the button is currently pressed.
        """
        super().__init__(window, text=text, bg=bg_color, command=self.on_click)
        self.grid(row=8-k_value[0], column=k_value[1], sticky="nsew")  # Position the button
        self.bg_color = bg_color
        self.k_value = k_value
        self.chessboard = chessboard
        self.is_pressed = is_pressed
        self.all_buttons.update([(k_value, self)])  # Add this button to the global button dictionary

    def on_click(self) -> None:
        """
        Handles the button click event. Toggles the selection of the button, 
        highlights valid moves for the associated piece, and manages button states and execute the move.
        """
        
        self.execute_move()

        if Custom_Button.last_button == self:
            # If the same button is clicked again, reset its state
            self.reset_highlights()
            Custom_Button.last_button = None
            return

        # Clear the selection of the last button
        self.clear_last_selection()

        # If the current button represents a piece, mark it and highlight valid moves
        if self.has_piece():
            Custom_Button.last_button = self
            self.config(bg="Blue", relief=RAISED)
            self.highlight_valid_moves()

    def execute_move(self) -> None:
        """
        Executes a move if the current button represents a valid destination.

        This method checks if the clicked button is one of the valid move buttons 
        highlighted previously. If valid, it updates the chessboard state, moves the piece, 
        and updates the button labels to reflect the new positions.

        Returns:
            None
        """
        for i in self.last_move_buttons:
            # Check if the current button is a valid move and the destination is part of the chessboard
            if self == i and self.k_value in self.chessboard:
                # Execute the move for the selected piece
                self.last_button.chessboard[self.last_button.k_value].execute_valid_move(self.k_value, self.chessboard)

                # Update the text of the original button to reflect the cleared position
                self.all_buttons[self.last_button.k_value].config(text=self.last_button.k_value)

                # Update the text of the current button to reflect the moved piece
                self.config(text=self.chessboard[self.k_value].name)

    def reset_highlights(self) -> None:
        """
        Resets the button's state and clears all highlighted valid moves.
        """
        # Reset the button's background and relief
        self.config(bg=self.bg_color, relief=FLAT)

        # Reset all buttons that were previously highlighted
        for button in self.last_move_buttons:
            button.config(bg=button.bg_color)
        
        # Clear the list of last move buttons
        self.last_move_buttons.clear()

    def clear_last_selection(self) -> None:
        """
        Clears the selection of the previously clicked button, if any.
        """
        if Custom_Button.last_button:
            # Reset the previous button's highlights and state
            Custom_Button.last_button.reset_highlights()
            Custom_Button.last_button = None

    def has_piece(self) -> bool:
        """
        Checks if the current button represents a square with a chess piece.

        Returns:
            bool: True if a piece is present, False otherwise.
        """
        return self.chessboard.get(self.k_value) is not None

    def highlight_valid_moves(self) -> None:
        """
        Highlights the valid moves for the chess piece associated with the button.

        Raises:
            ValueError: If the calculate_valid_moves method does not return a list.
        """
        valid_moves = self.chessboard[self.k_value].calculate_valid_moves(self.chessboard)

        # Ensure valid_moves is a list
        if not isinstance(valid_moves, list):
            raise ValueError("calculate_valid_moves must return a list of moves")

        # Highlight each valid move
        for move in valid_moves:
            if move in self.all_buttons:
                target_button = self.all_buttons[move]
                target_button.config(bg="yellow")
                self.last_move_buttons.append(target_button)