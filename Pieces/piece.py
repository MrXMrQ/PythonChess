from GUI.custom_banner import CustomBanner

class Piece:
    """
    Represents a chess piece with its attributes and behavior.
    
    Attributes:
        _name (str): The name of the piece.
        _start_field (tuple): The starting position of the piece on the board.
        _directions (list): A list of movement directions allowed for this piece.
        _score (int): The score value of the piece.
        _team (str): The team the piece belongs to ("white" or "black").
        _current_field (tuple): The current position of the piece on the board.
        _last_field (tuple): The last position of the piece before moving.
        _moved (bool): Whether the piece has moved from its starting position.

    Methodes:
        compute_moves(self, chessboard: dict) -> list:
            Computes all valid moves for the basic piece based on the current chessboard state.

        apply_move(self, chessboard: dict, field: tuple, banner: CustomBanner) -> dict:
            Applies a move to the piece and updates the chessboard.

        __str__(self) -> str:
            Returns a string representation of the piece.
    """

    def __init__(self, name: str, start_field: tuple, directions: list, score: int, team: str = "white") -> None:
        if not isinstance(name, str):
            raise TypeError(f"ERROR: 'name' must be type 'str' not {type(name)}")
        
        if not isinstance(start_field, tuple):
            raise TypeError(f"ERROR: 'start_field' must be type 'tuple' not {type(start_field)}")
        
        if not isinstance(directions, list):
            raise TypeError(f"ERROR: 'move_directions' must be type 'list' not {type(directions)}")
        
        if not isinstance(score, int):
            raise TypeError(f"ERROR: 'score' must be type 'int' not {type(score)}")
        
        if not isinstance(team, str):
            raise TypeError(f"ERROR: 'is_friend' must be type 'str' not {type(team)}")
        
        if team not in {"white", "black"}:
            raise ValueError(f"ERROR: piece has no valid team: {self._team}")
        
        self._name = name
        self._start_field = start_field
        self._directions = directions
        self._score = score
        self._team = team

        self._current_field = start_field
        self._last_field = start_field
        self._moved = False

    def compute_moves(self, chessboard: dict) -> list:
        """
        Computes all valid moves for the basic piece based on the current chessboard state.

        Args:
            chessboard (dict): The current state of the chessboard, mapping positions to pieces.

        Returns:
            list: A list of valid moves as tuples.

        Raises:
            TypeError: If chessboard is not a dictionary.
        """

        if not isinstance(chessboard, dict):
            raise TypeError(f"ERROR: chessboard must be type 'dict' not {type(chessboard)}")

        valid_moves = []
    
        for direction in self._directions:
            row, col = self.current_field

            while True:
                row += direction[0]
                col += direction[1]
                next_field = (row, col)

                if next_field not in chessboard:
                    break

                piece_at_field = chessboard[next_field]

                if piece_at_field is None:
                    valid_moves.append(next_field)
                    continue   

                if piece_at_field._team != self._team:
                    valid_moves.append(next_field)   

                break

        return valid_moves
    
    def apply_move(self, chessboard: dict, field: tuple, banner: CustomBanner) -> dict:
        """
        Applies a move to the piece and updates the chessboard.

        Args:
            field (tuple): The new position for the piece.
            chessboard (dict): The current state of the chessboard.
            banner (CustomBanner): A banner object to update scores if a piece is captured.

        Returns:
            dict: The updated chessboard.

        Raises:
            KeyError: If the target field is not on the chessboard.
        """

        if not isinstance(chessboard, dict):
            raise TypeError(f"ERROR: chessboard must be type 'dict' not {type(chessboard)}")
        
        if not isinstance(field, tuple):
            raise  TypeError(f"ERROR: field must be type 'tuple' not {type(field)}")
        
        if not isinstance(banner, CustomBanner):
            raise  TypeError(f"ERROR: banner must be type 'CustomBanner' not {type(banner)}")
        
        if field not in chessboard:
            raise KeyError(f"ERROR: Target field {field} is not on the chessboard.")
        
        target_piece = chessboard[field]

        if target_piece is not None:
            banner.update_scorepoint(target_piece._score, self._team)

        self._moved = True
        chessboard[field], chessboard[self._current_field] = chessboard[self._current_field], None
        self._last_field, self._current_field = self._current_field, field
        
        return chessboard

    def __str__(self) -> str:
        """
        Returns a string representation of the piece.
        """

        return f"Name: {self._name}, Start field: {self._start_field}, Current field: {self._current_field}, Last field: {self._last_field}, Friend: {self._team}"
    
    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter
    def name(self, other: str) -> None:
        if not isinstance(other, str):
            raise TypeError(f"ERROR: can't set name {self} because: 'name' must be type 'str' not {type(other)}")
        
        self._name = other

    @property
    def start_field(self) -> str:
        return self._start_field

    @property
    def current_field(self) -> tuple:
        return self._current_field
    
    @current_field.setter
    def current_field(self, other: tuple) -> None:
        if not isinstance(other, tuple):
            raise TypeError(f"ERROR: can't set current_field {self} because: 'current_field' must be type 'tuple' not {type(other)}")

        self._current_field = other

    @property
    def last_field(self) -> tuple:
        return self._last_field
    
    @last_field.setter
    def last_field(self, other) -> None:
        if not isinstance(other, tuple):
            raise TypeError(f"ERROR: 'last_field' must be type 'tuple' not {type(other)}")

        self._last_field = other

    @property
    def directions(self) -> list:
        return self._directions
    
    @property
    def score(self) -> int:
        return self._score

    @property
    def team(self) -> str:
        return self._team
    
    @property
    def moved(self) -> bool:
        return self._moved
    
    @moved.setter
    def moved(self, other) -> None:
        if not isinstance(other, bool):
            raise TypeError(f"ERROR: can't set first_move {self} because: 'first_move' must be type 'bool' not type {type(other)}")
        
        self._moved = other