from tkinter import RAISED, Button
from tkinter import Tk
from Pieces.pawn import Pawn

class CustomButton(Button):
    _all_buttons: dict = {}
    _last_highlighted_buttons: list = []
    _last_button = None

    def __init__(self, window: Tk, text: str, bg_color: str, k_value: tuple, chessboard: dict) -> None:
        super().__init__(window, text=text, bg=bg_color, command=self.on_click, font=('Helvetica', 30, 'bold'), relief=RAISED)

        self._bg_color = bg_color
        self._key_value = k_value
        self._chessboard = chessboard
        self.grid(row=8-k_value[0], column=k_value[1], sticky="nsew")

        CustomButton._all_buttons.update([(k_value, self)])

    def on_click(self) -> None:
        self._move()

        if CustomButton._last_button:
            CustomButton._last_button.config(bg=CustomButton._last_button._bg_color)
            CustomButton._last_button = None
            self._reset()
        
        if self._has_piece():
            CustomButton._last_button = self
            self.config(bg="Blue")
            self._highlight()

    def _has_piece(self) -> bool:
        return self._chessboard.get(self._key_value) is not None
    
    def _reset(self) -> None:
        self.config(bg=self._bg_color)

        for i in CustomButton._last_highlighted_buttons:
            if i._chessboard[i._key_value] is None:
                i.config(text="")
            else:
                i.config(bg=i._bg_color)

        CustomButton._last_highlighted_buttons.clear()

    def _highlight(self) -> None:
        valid_moves = self._chessboard[self._key_value].compute_moves(self._chessboard)

        for move in valid_moves:
            target_button = self._all_buttons[move]
            if target_button._chessboard[move] is None:
                target_button.config(text="•")
            else:
                target_button.config(bg="Yellow", )        
            self._last_highlighted_buttons.append(target_button)    
    
    def _move(self) -> None:
        for i in self._last_highlighted_buttons:
            if self == i and self._key_value in self._chessboard:
                # Check for Pawn to change first move
                if isinstance(self._last_button._chessboard[self._last_button._key_value], Pawn):
                    self._last_button._chessboard[self._last_button._key_value].first_move = True    

                self._last_button._chessboard[self._last_button._key_value].apply_move(self._key_value, self._chessboard)
                self._all_buttons[self._last_button._key_value].config(text="")
                self.config(text=self._chessboard[self._key_value].name)