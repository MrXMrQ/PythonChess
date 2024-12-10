from MyFigure import Figure

class Pawn(Figure):
    def __init__(self, name: str, start_field: tuple, is_Friend: bool = True, first_move: bool = True, is_at_end: bool = False) -> None:
        super().__init__(name, start_field, is_Friend)
        self.first_move = first_move
        self.is_at_end = is_at_end

    def move(self, move_to_field: tuple):
        old_x, old_y = self.current_field
        new_x, new_y = move_to_field

        if self.is_at_end:
            print("END")
            return

        if self.first_move:
            if old_x == new_x and new_y > old_y and new_y - old_y == 2 or new_y - old_y == 1:
                self.first_move = False
                self.current_field = move_to_field
                print("Valid field {}".format(move_to_field))
            else:
                print("Invalid field {} on first move".format(move_to_field))

        elif old_x == new_x and new_y > old_y and new_y - old_y == 1:

            if  move_to_field[1] == 8:
                self.current_field = move_to_field
                self.is_at_end = True
                print("Valid field {}".format(move_to_field))
                print("Chosse")
                return
            
            self.current_field = move_to_field
            print("Valid field {}".format(move_to_field))

        else:
            print("Invalid field {}".format(move_to_field))

    def get_Field(self) -> tuple:
        return self.current_field