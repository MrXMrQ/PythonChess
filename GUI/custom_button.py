
from tkinter import RAISED, Button

from GUI import chessboard
from Pieces.piece import Piece
from Pieces.rook import Rook
from Pieces.king import King

from GUI.chessboard import Chessboard

class CustomButton(Button):
    _button_registry: dict = {}
    _marked_buttons: list= []
    _move_options: list = []
    _last_button = None

    def __init__(self, content: Piece, chessboard_console: Chessboard, root, grid) -> None:
        self._content = content
        self._chessboard_console = chessboard_console
        self._bg = "lightgray" if (grid[0] + grid[1]) % 2 == 0 else "gray"
        self._grid = grid

        super().__init__(master=root, 
                         text=content.name if content is not None else "", 
                         bg=self._bg, 
                         command=self._on_left_click, 
                         font=('Helvetica', 30, 'bold'), 
                         relief=RAISED
                        )
        self.grid(row=8-grid[0], column=grid[1], sticky="nsew")
        self.bind("<Button-3>", self._on_right_click)
        CustomButton._button_registry.update([(grid, self)])

    def _on_right_click(self, event) -> None:
        if self in CustomButton._marked_buttons:
            self.config(bg=self._bg)
            CustomButton._marked_buttons.remove(self)
            return
        
        CustomButton._marked_buttons.append(self)
        self.config(bg="Green")

    def _on_left_click(self) -> None:
        self._move()

        if CustomButton._last_button:
            if CustomButton._last_button == self:
                self.config(bg=self._bg)
                CustomButton._last_button = None
            else:
                CustomButton._last_button.config(bg=CustomButton._last_button._bg)
                CustomButton._last_button = None

            self._reset_hightlight()

        # highlight move for selected piece
        if self._content is not None:
            CustomButton._last_button = self
            self.config(bg="Blue")
            self._hightlight()

    def _hightlight(self) -> None:
        valid_moves = self._content.compute_moves(Chessboard.chessboard)

        if isinstance(self._content, Rook):
            if self._content.castle(Chessboard.chessboard) is not None:
                valid_moves.append(self._content.castle(Chessboard.chessboard))

        for move in valid_moves:
            button = CustomButton._button_registry[move]

            if Chessboard.chessboard[move] is None:
                button.config(text="•")
            else:
                button.config(bg="Yellow")

            self._move_options.append(button)
            
    def _reset_hightlight(self) -> None:
        self.config(bg=self._bg)

        for button in CustomButton._move_options:
            if Chessboard.chessboard[button._grid] is None:
                button.config(text="")
            else:
                button.config(bg=button._bg)

        CustomButton._move_options.clear()

    def _move(self) -> None:
        # reset buttons that are marked with right click
        for button in CustomButton._marked_buttons:
            button.config(bg=button._bg)

        CustomButton._marked_buttons.clear()

        # perform move
        for button in CustomButton._move_options:
            if self == button:
                # castle check
                if isinstance(CustomButton._last_button._content, Rook) and isinstance(self._content, King):
                    values = CustomButton._last_button._content.apply_move(self._grid, Chessboard.chessboard)
                    Chessboard.chessboard = values[0]

                    self.config(text="")
                    CustomButton._last_button.config(text="")
                    self._content = None
                    CustomButton._last_button._content = None

                    b1 = CustomButton._button_registry[values[1]]
                    b2 = CustomButton._button_registry[values[2]]

                    b1._content = Chessboard.chessboard[values[1]]
                    b2._content = Chessboard.chessboard[values[2]]
                    b1.config(text=b1._content.name)
                    b2.config(text=b2._content.name)

                    print(self._chessboard_console)

                    return
                
                # we have to move the conteten from the last button to the new button
                self._content = CustomButton._last_button._content
                CustomButton._last_button._content = None

                self._content.moved = True
                Chessboard.chessboard = self._content.apply_move(self._grid, Chessboard.chessboard)

                # console chessboard
                print(self._chessboard_console)

                CustomButton._last_button.config(text="")
                self.config(text=self._content.name)