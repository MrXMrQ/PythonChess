class Figure:
    """
    Represents a figure in a game or simulation, such as a chess piece or a game character.

    Attributes:
        name (str): The name of the figure.
        start_field (tuple): The starting position of the figure as a tuple of coordinates (e.g., (x, y)).
        current_field (tuple): The current position of the figure as a tuple of coordinates.
        is_Friend (bool): A flag indicating if the figure is a friendly entity. Defaults to True.
    """

    def __init__(self, name: str, start_field: tuple, current_field: tuple, is_Friend: bool = True) -> None:
        """
        Initializes a new instance of the Figure class.

        Args:
            name (str): The name of the figure.
            start_field (tuple): The starting position of the figure as a tuple of coordinates.
            current_field (tuple): The current position of the figure as a tuple of coordinates.
            is_Friend (bool): A flag indicating if the figure is friendly. Defaults to True.
        """
        
        self.name = name
        self.start_field = start_field
        self.current_field = start_field
        self.is_Friend = is_Friend
        