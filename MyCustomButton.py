from tkinter import *

class Custom_Button(Button):
    last_button = None

    def __init__(self, window, text: str, bg_color: str, k_value: tuple, chessboard: dict, is_pressed: bool = False):
        super().__init__(window, text=text, bg=bg_color, command=self.on_click)
        self.grid(row=8-k_value[0], column=k_value[1], sticky="nsew")
        self.bg_color = bg_color
        self.k_value = k_value
        self.chessboard = chessboard
        self.is_pressed = is_pressed
        
    def on_click(self):
        if Custom_Button.last_button == self:
            self.config(bg=self.bg_color)
            Custom_Button.last_button = None
        else:
            if Custom_Button.last_button:
                Custom_Button.last_button.config(bg=Custom_Button.last_button.bg_color)

            Custom_Button.last_button = self
            self.config(bg="lightblue", relief=RAISED)

        print(self.chessboard[self.k_value])