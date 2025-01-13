class Piece:
    """
    Represents a figure in a game or simulation, such as a chess piece or a game character.

    Attributes:
        name (str): The name of the figure.
        start_field (tuple): The starting position of the figure as a tuple of coordinates (e.g., (x, y)).
        current_field (tuple): The current position of the figure as a tuple of coordinates.
        is_Friend (bool): A flag indicating if the figure is a friendly entity. Defaults to True.
    """

    def __init__(self, name: str, start_field: tuple, is_Friend: bool = True) -> None:
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
        self._is_Friend = is_Friend

    def __str__(self) -> str:
        return "{} {} {} {}".format(self._name, self._start_field, self._current_field, self._is_Friend)
    
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
    def is_Friend(self) -> str:
        return self._is_Friend
    
    @is_Friend.setter
    def is_Friend(self, is_Friend: str) -> None:
        self._is_Friend = is_Friend