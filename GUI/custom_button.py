
from cgitb import text
from tkinter import NO, RAISED, Button

from Pieces.piece import Piece
from Pieces.rook import Rook
from Pieces.king import King

from GUI.custom_banner import CustomBanner
from GUI.chessboard import Chessboard


class CustomButton(Button):
    _button_registry: dict = {}
    _marked_buttons: list= []
    _move_options: list = []
    _last_button = None

    def __init__(self, content: Piece, chessboard_console: Chessboard, banner: CustomBanner, root, grid) -> None:
        self._content = content
        self._chessboard_console = chessboard_console
        self._banner = banner
        self._bg = "#efdab6" if (grid[0] + grid[1]) % 2 == 0 else "#b58963"
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
        if self._move():
            print(f"\n{self._chessboard_console}")
            self._reset_hightlight()
            return

        if self._track_turn():
            return

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

    def _track_turn(self) -> bool:
        if self._content is None:
            return False

        turn_white = Chessboard.turn % 2 == 0
        piece_white = self._content._team == "white"
        piece_black = self._content._team == "black"

        if turn_white:
            if not piece_white:
                self._banner.change_text("It's White's turn, not Black's.", None)
                return True
            self._banner.change_text(f"White selects the piece", (self._content.name, self._content._last_field, self._content.current_field))
        else:
            if not piece_black:
                self._banner.change_text("It's Black's turn, not White's.", None)
                return True
            self._banner.change_text(f"Black selects the piece", (self._content.name, self._content._last_field, self._content.current_field))

        return

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

        if CustomButton._last_button:
            CustomButton._last_button.config(text="", bg=CustomButton._last_button._bg)
            CustomButton._last_button = None

        for button in CustomButton._move_options:
            if Chessboard.chessboard[button._grid] is None:
                button.config(text="")
            else:
                button.config(bg=button._bg)

        CustomButton._move_options.clear()

    def _move(self) -> bool:
        

        # reset buttons that are marked with right click
        for button in CustomButton._marked_buttons:
            button.config(bg=button._bg)

        CustomButton._marked_buttons.clear()

        # perform move
        for button in CustomButton._move_options:
            if self == button:
                Chessboard.turn += 1
                player = "White" if Chessboard.turn % 2 == 1 else "Black"

                # castle check
                if isinstance(CustomButton._last_button._content, Rook) and isinstance(self._content, King):
                    values = CustomButton._last_button._content.apply_move(self._grid, Chessboard.chessboard, self._banner)
                
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

                    self._banner.change_text(f"{player} CASTLE", None)

                    return True
                
                self._content = CustomButton._last_button._content
                CustomButton._last_button._content = None

                self._content.moved = True
                Chessboard.chessboard = self._content.apply_move(self._grid, Chessboard.chessboard, self._banner)

                CustomButton._last_button.config(text="")
                self.config(text=self._content.name)

                self.config(bg=self._bg)

                player = "White" if Chessboard.turn % 2 == 1 else "Black"
                self._banner.change_text(f"{player} moved piece", (self._content.name, self._content._last_field, self._content.current_field))

                return True