class Figure:
    def __init__(self, name: str, start_field: tuple, current_field: tuple, is_Friend: bool = True) -> None:
        self.name = name
        self.start_field = start_field
        self.current_field = start_field
        self.is_Friend = is_Friend
        