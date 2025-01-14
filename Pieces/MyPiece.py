class Piece:
    """
    Represents a figure in a game or simulation, such as a chess piece or a game character.

    Attributes:
        name (str): The name of the figure.
        start_field (tuple): The starting position of the figure as a tuple of coordinates (e.g., (x, y)).
        current_field (tuple): The current position of the figure as a tuple of coordinates.
        is_Friend (bool): A flag indicating if the figure is a friendly entity. Defaults to True.
    """

    def __init__(self, name: str, start_field: tuple, move_directions: list, is_friend: bool, has_limit: bool = False, is_pawn: bool = False, first_move: bool = False) -> None:
        """
        Initializes a new instance of the Figure class.

        Args:
            name (str): The name of the figure.
            start_field (tuple): The starting position of the figure as a tuple of coordinates.
            current_field (tuple): The current position of the figure as a tuple of coordinates.
            is_Friend (bool): A flag indicating if the figure is friendly. Defaults to True.
        """
        
        self._name = name
        self._start_field = start_field
        self._current_field = start_field
        self._move_directions = move_directions
        self._is_friend = is_friend
        self._has_limit = has_limit
        self._is_pawn = is_pawn
        self._first_move = first_move

    def calculate_valid_moves(self, chessboard: dict) -> list:
        """
        Calculate all valid moves for a chess piece on a given chessboard.

        This method determines the possible moves for a chess piece based on its 
        type, position, and the state of the chessboard. The movement logic accounts 
        for pawns, limited-movement pieces (e.g., king, knight), and unlimited-movement 
        pieces (e.g., bishop, rook, queen).

        Args:
            chessboard (dict): A dictionary representing the chessboard. The keys are 
                               tuples (row, col) indicating the position, and the values 
                               are either `None` (empty square) or an object representing 
                               a chess piece.

        Returns:
            list: A list of tuples representing valid target positions for the chess piece.

        Behavior:
            - For pawns (self.is_pawn), the method delegates to self.pawn_moves, 
              which calculates pawn-specific moves (e.g., forward, capture).
            - For pieces with limited movement (self.has_limit), valid moves are 
              determined by adding the piece's directional offsets to its current position.
            - For pieces with unlimited movement, the method iterates through each 
              direction and appends valid moves until blocked by another piece or 
              the edge of the board.

        Constraints:
            - A move is valid if the target square is empty or contains an enemy piece.
            - The method stops calculating further moves along a direction when a 
              piece is encountered (either friendly or enemy).
        """
        
        valid_moves = []
        directions = self.move_directions
        
        if self.is_pawn:
            return self.pawn_moves(chessboard)
        
        if self.has_limit:
            row, col = self.current_field

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                next_field = (new_row, new_col)

                if next_field in chessboard:
                    if chessboard[next_field] is None or not chessboard[next_field].is_friend:
                        valid_moves.append(next_field)

            return valid_moves

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
    
    def pawn_moves(self, chessboard: dict) -> list:
        """
        Calculate all valid moves for a pawn on a given chessboard.

        This method determines the possible moves for a pawn based on its current 
        position, the state of the chessboard, and whether it has moved before.

        Args:
            chessboard (dict): A dictionary representing the chessboard. The keys are 
                               tuples (row, col) indicating the position, and the values 
                               are either None (empty square) or an object representing 
                               a chess piece.

        Returns:
            list: A list of tuples representing valid target positions for the pawn.

        Behavior:
            - Pawns can move one step forward if the square is empty.
            - On their first move, pawns can move two steps forward if both squares 
              are empty.
            - Pawns can capture diagonally to the left or right if an enemy piece 
              occupies the target square.
            - Moves are constrained by the boundaries of the board and the presence 
              of other pieces.
        """

        valid_moves = []
        row, col = self.current_field
    
        one_step = (row + 1, col)
        if one_step in chessboard and chessboard[one_step] is None:
            valid_moves.append(one_step)

            two_steps = (row + 2, col)
            if not self._first_move and two_steps in chessboard and chessboard[two_steps] is None:
                valid_moves.append(two_steps)

        diagonal_left = (row + 1, col - 1)
        diagonal_right = (row + 1, col + 1)

        if diagonal_left in chessboard and chessboard[diagonal_left] is not None:
            if not chessboard[diagonal_left].is_friend:
                valid_moves.append(diagonal_left)

        if diagonal_right in chessboard and chessboard[diagonal_right] is not None:
            if not chessboard[diagonal_right].is_friend:
                valid_moves.append(diagonal_right)

        return valid_moves
    
    def execute_valid_move(self, field: tuple, chessboard: dict) -> None:
        """
        Execute a valid move for the chess piece, updating its position and the chessboard.

        This method moves the chess piece to the specified target field, updates the 
        chessboard to reflect the change, and marks the piece as having made its first move.

        Args:
            field (tuple): The target position as a tuple (row, col).
            chessboard (dict): A dictionary representing the chessboard. The keys are 
                               tuples (row, col) indicating the position, and the values 
                               are either `None` (empty square) or an object representing 
                               a chess piece.

        Returns:
            None: The method modifies the chessboard and the piece's state in place.

        Behavior:
            - If the target field is valid (exists in the chessboard), the method:
                1. Sets the current field on the chessboard to None.
                2. Updates the piece's current_field to the target field.
                3. Marks first_move as True (only important for pawn).
                4. Places the piece at the new position on the chessboard.
        """

        if field in chessboard:
            chessboard[self.current_field] = None
            self.current_field = field
            self.first_move = True
            chessboard[field] = self

        return chessboard

    def __str__(self) -> str:
        return "{} {} {} {}".format(self._name, self._start_field, self._current_field, self._is_friend)
    
    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def start_field(self) -> str:
        return self._start_field
    
    @start_field.setter
    def start_field(self, start_field: str) -> None:
        self._start_field = start_field

    @property
    def current_field(self) -> str:
        return self._current_field
    
    @current_field.setter
    def current_field(self, current_field: str) -> None:
        self._current_field = current_field

    @property
    def move_directions(self) -> list:
        return self._move_directions
    
    @move_directions.setter
    def move_directions(self, move_directions) -> None:
        self._move_directions = move_directions

    @property
    def is_friend(self) -> str:
        return self._is_friend
    
    @is_friend.setter
    def is_friend(self, is_Friend: str) -> None:
        self._is_friend = is_Friend

    @property
    def has_limit(self) -> bool:
        return self._has_limit
    
    @has_limit.setter
    def has_limit(self, has_limit: bool) -> None:
        self._has_limit = has_limit

    @property
    def is_pawn(self) -> bool:
        return self._is_pawn
    
    @is_pawn.setter
    def is_pawn(self, is_pawn: bool) -> None:
        self._is_pawn = is_pawn

    @property
    def first_move(self) -> bool:
        return self._first_move
    
    @first_move.setter
    def first_move(self, first_move: bool) -> None:
        self._first_move = first_move