class Piece:
    def __init__(self, name: str, start_field: tuple, move_directions: list, is_friend: bool = True) -> None:
        if not isinstance(name, str):
            raise TypeError(f"ERROR: 'name' must be type 'str' not {type(name)}")
        
        if not isinstance(start_field, tuple):
            raise TypeError(f"ERROR: 'start_field' must be type 'tuple' not {type(start_field)}")
        
        if not isinstance(move_directions, list):
            raise TypeError(f"ERROR: 'move_directions' must be type 'list' not {type(start_field)}")
        
        if not isinstance(is_friend, bool):
            raise TypeError(f"ERROR: 'is_friend' must be type 'bool' not {type(start_field)}")
        
        self._name = name
        self._start_field = start_field
        self._current_field = start_field
        self._directions = move_directions
        self._is_friend = is_friend

    def compute_moves(self, chessboard: dict) -> list:
        if not isinstance(chessboard, dict):
            raise ValueError(f"ERROR: chessboard must be type 'dict' not {type(chessboard)}")

        valid_moves = []
        directions = self.directions
    
        for direction in directions:
            row, col = self.current_field

            while True:
                row += direction[0]
                col += direction[1]
                next_field = (row, col)

                if next_field not in chessboard:
                    break

                if chessboard[next_field] is not None:
                    if not chessboard[next_field].is_friend:
                        valid_moves.append(next_field)
                    break 

                valid_moves.append(next_field)

        return valid_moves
    
    def apply_move(self, field: tuple, chessboard: dict) -> None:
        if field in chessboard:
            chessboard[self.current_field] = None
            self.current_field = field
            chessboard[field] = self

        return chessboard

    def __str__(self) -> str:
        return f"Name: {self._name}, Start field: {self._start_field}, Current field: {self._current_field} Friend: {self._is_friend}"
    
    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter
    def name(self, other: str) -> None:
        if not isinstance(other, str):
            raise TypeError(f"ERROR: 'name' must be type 'str' not {type(other)}")
        
        self._name = other

    @property
    def start_field(self) -> str:
        return self._start_field

    @property
    def current_field(self) -> str:
        return self._current_field
    
    @current_field.setter
    def current_field(self, other: tuple) -> None:
        if not isinstance(other, tuple):
            raise TypeError(f"ERROR: 'current_field' must be type 'tuple' not {type(other)}")

        self._current_field = other

    @property
    def directions(self) -> list:
        return self._directions

    @property
    def is_friend(self) -> str:
        return self._is_friend