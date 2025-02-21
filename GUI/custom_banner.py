from tkinter import Frame, Label
from typing import Iterable, Type

class CustomBanner(Frame):
    def __init__(self, master, bg: str) -> None:
        super().__init__(master, bg=bg)
        self.pack(fill="x")
        for i in range(1, 4):
            self.grid_columnconfigure(i, weight=1)

        self._text = "White"
        self._score_W = 0
        self._score_B = 0

        label_left = Label(self, text=f"W: {self._score_W}", bg=bg, fg="black", font=('Helvetica', 20, 'bold'), width=5)
        label_left.grid(row=0, column=1, sticky="nsew", padx=10)

        label_right = Label(self, text=f"B: {self._score_B}", bg=bg, fg="black", font=('Helvetica', 20, 'bold'), width=5)
        label_right.grid(row=0, column=3, sticky="nsew", padx=10)
        
        label_middle = Label(self, text=f"{self._text}", bg=bg, fg="black", font=('Helvetica', 20, 'bold'),wraplength=350, height=2, width=15)
        label_middle.grid(row=0, column=2, sticky="nsew", padx=10)
        
        self._label_left = label_left
        self._label_middle = label_middle
        self._label_right = label_right

    def change_text(self, text: str, data) -> None:
        if not isinstance(text, str):
            raise ValueError(f"ERROR: Cant change text from 'middle_label' becuase 'text' is not  type str: {type(text)}")
        
        if data is None:
            self._label_middle.config(text=text)  
            return
        
        name, last_field, new_field = data

        if "moved" in text:
            self._label_middle.config(text=text + f"\n {name} from {last_field} to {new_field}")
            return
        
        self._label_middle.config(text=text + f"\n {name} {last_field}")

    def update_scorepoint(self, points: int, team: str) -> None:
        if not isinstance(points, int):
            raise TypeError(f"ERROR: cant add point, points must be type 'int' not : {type(points)}")
        
        if not isinstance(team, str):
            raise TypeError(f"ERROR: cant compare team, team must be type 'str' not : {type(team)}")

        if team == "white":
            self._score_W += points
            self._label_left.config(text=f"W: {self._score_W}")
        elif team == "black":
            self._score_B += points
            self._label_right.config(text=f"B: {self._score_B}")
        else:
            raise ValueError(f"Unknown team {team}")