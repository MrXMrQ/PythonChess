from tkinter import RAISED, Button

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
        self._grid = grid

        super().__init__(master=root, 
                         text=content.name if content is not None else "", 
                         bg=self._get_background_color(grid), 
                         command=self._on_left_click, 
                         font=('Helvetica', 30, 'bold'), 
                         relief=RAISED
                        )
        self.grid(row=8-grid[0], column=grid[1], sticky="nsew")
        self.bind("<Button-3>", self._on_right_click)
        CustomButton._button_registry[grid] = self

    def __str__(self) -> str:
        return f"Content: {self._content}, Grid: {self._grid}"
    
    @staticmethod
    def _get_background_color(grid) -> str:
        return "#efdab6" if (grid[0] + grid[1]) % 2 == 0 else "#b58963"

    def _on_right_click(self, event) -> None:
        if self in CustomButton._marked_buttons:
            self._unmark_button()
        else:
            self._mark_button()
        
        CustomButton._marked_buttons.append(self)
        self.config(bg="Green")

    def _mark_button(self) -> None:
        CustomButton._marked_buttons.append(self)
        self.config(bg="Green")

    def _unmark_button(self) -> None:
        self.config(bg=self._get_background_color(self._grid))
        CustomButton._marked_buttons.remove(self)

    def _on_left_click(self) -> None:
        if self._move():
            print(f"\n{self._chessboard_console}")
            self._reset_highlight()
            return
        
        if self._track_turn():
            return

        self._handle_selection()

    def _track_turn(self) -> bool:
        if not self._content:
            return False

        is_white_turn = Chessboard.turn % 2 == 0
        piece_team = self._content._team

        if (is_white_turn and piece_team != "white") or (not is_white_turn and piece_team != "black"):
            self._banner.change_text(f"It's {'White' if is_white_turn else 'Black'}'s turn, not {piece_team.capitalize()}.", None)
            return True

        self._banner.change_text(f"{piece_team.capitalize()} selects the piece", (self._content.name, self._content._last_field, self._content.current_field))
        return False
    
    def _handle_selection(self) -> None:
        if CustomButton._last_button:
            CustomButton._last_button.config(bg=CustomButton._last_button._get_background_color(CustomButton._last_button._grid))
            CustomButton._last_button = None
            self._reset_highlight()
        
        if self._content:
            CustomButton._last_button = self
            self.config(bg="Blue")
            self._highlight_moves()    

    def _highlight_moves(self) -> None:
        valid_moves = self._content.compute_moves(Chessboard.chessboard)

        if isinstance(self._content, Rook):
            castling_move = self._content.castle(Chessboard.chessboard)
            if castling_move:
                valid_moves.append(castling_move)

        for move in valid_moves:
            button = CustomButton._button_registry.get(move)
            if button:
                if Chessboard.chessboard[move] is None:
                    button.config(text="•", bg=button._get_background_color(button._grid))
                else:
                    button.config(bg="Yellow")
                CustomButton._move_options.append(button)

        return
            
    def _reset_highlight(self) -> None:
        self.config(bg=self._get_background_color(self._grid))

        if CustomButton._last_button:
            CustomButton._last_button.config(text="", bg=CustomButton._last_button._get_background_color(CustomButton._last_button._grid))
            CustomButton._last_button = None

        for button in CustomButton._move_options:
            if Chessboard.chessboard[button._grid] is None:
                button.config(text="")
            else:
                button.config(bg=button._get_background_color(self._grid))

        CustomButton._move_options.clear()

    def _move(self) -> bool:
        for button in CustomButton._marked_buttons:
            button.config(bg=button._get_background_color(button._grid))
        CustomButton._marked_buttons.clear()

        for button in CustomButton._move_options:
            if self == button:
                return self._execute_move()
        
        return False
            
    def _execute_move(self) -> bool:
        Chessboard.turn += 1
        player = "White" if Chessboard.turn % 2 == 1 else "Black"
        
        if isinstance(CustomButton._last_button._content, Rook) and isinstance(self._content, King):
            self.config(bg="Yellow")  # Highlight castling move
            return self._handle_castling(player)
        
        self._content = CustomButton._last_button._content
        CustomButton._last_button._content = None
        self._content.moved = True
        Chessboard.chessboard = self._content.apply_move(self._grid, Chessboard.chessboard, self._banner)
        
        CustomButton._last_button.config(text="")
        self.config(text=self._content.name, bg=self._get_background_color(self._grid))
        print(self._content)
        self._banner.change_text(f"{player} moved piece", (self._content.name, self._content._last_field, self._content.current_field))
        
        self._reset_highlight()  # Reset background colors after move
        return True
    
    def _handle_castling(self, player: str) -> bool:
        values = CustomButton._last_button._content.apply_move(self._grid, Chessboard.chessboard, self._banner)
        Chessboard.chessboard = values[0]
        self._update_castling_buttons(values[1], values[2])
        self._banner.change_text(f"{player} CASTLE", None)
        return True

    def _update_castling_buttons(self, rook_pos, king_pos):
        for pos in [rook_pos, king_pos]:
            button = CustomButton._button_registry[pos]
            button._content = Chessboard.chessboard[pos]
            button.config(text=button._content.name)