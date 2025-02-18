class Piece:
    def __init__(self, name: str, start_field: tuple, move_directions: list, team: str = "white") -> None:
        if not isinstance(name, str):
            raise TypeError(f"ERROR: 'name' must be type 'str' not {type(name)}")
        
        if not isinstance(start_field, tuple):
            raise TypeError(f"ERROR: 'start_field' must be type 'tuple' not {type(start_field)}")
        
        if not isinstance(move_directions, list):
            raise TypeError(f"ERROR: 'move_directions' must be type 'list' not {type(start_field)}")
        
        if not isinstance(team, str):
            raise TypeError(f"ERROR: 'is_friend' must be type 'str' not {type(start_field)}")
        
        self._name = name
        self._start_field = start_field
        self._current_field = start_field
        self._directions = move_directions
        self._team = team
        self._moved = False

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
                    if self._team == "white":
                        if not chessboard[next_field]._team == "white":
                            valid_moves.append(next_field)
                        break
                    elif self._team == "black":
                        if not chessboard[next_field]._team == "black":
                            valid_moves.append(next_field)
                        break
                    else:
                        raise ValueError(f"ERROR: object have no team: {self._team}")

                valid_moves.append(next_field)

        return valid_moves
    
    def apply_move(self, field: tuple, chessboard: dict) -> None:
        if field in chessboard:
            chessboard[self.current_field] = None
            self.current_field = field
            chessboard[field] = self

        return chessboard

    def __str__(self) -> str:
        return f"Name: {self._name}, Start field: {self._start_field}, Current field: {self._current_field} Friend: {self._team}"
    
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
    def team(self) -> str:
        return self._team
    
    @property
    def moved(self) -> bool:
        return self._moved
    
    @moved.setter
    def moved(self, other) -> None:
        if not isinstance(other, bool):
            raise ValueError(f"ERROR: 'first_move' must be type 'bool' not type {type(other)}")
        
        self._moved = other