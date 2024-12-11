from MyPawn import Pawn

class Test_Figures:
    """
    A class to test the functionality and behavior of chess pieces.

    Attributes:
        pawns (list): A list of Pawn objects to be tested.
        rooks (list): A list of Rook objects to be tested (not implemented yet).
    """

    def __init__(self, pawns: list, rooks: list):
        """
        Initializes the Test_Figures instance with lists of pawns and rooks.

        Args:
            pawns (list): A list of Pawn objects to be tested.
            rooks (list): A list of Rook objects to be tested.
        """

        self.pawns = pawns
        self.rooks = rooks

    def pawn_test(self) -> None:
        """
        Executes all tests for Pawn objects, including start field, movement, and attack tests.
        Prints results for each test and a summary upon successful completion.
        """

        print("---------------------------- \nPawn:")
        self.pawn_start_field()
        self.pawn_movement()
        self.pawn_attack()
        print("Passed all the pawn tests! \n----------------------------")

    def pawn_start_field(self) -> None:
        """
        Tests whether each pawn starts on its correct initial field.

        Asserts:
            Each Pawn object's start_field matches the expected initial field.
        """

        for i in range(len(self.pawns)):
            assert self.pawns[i].start_field == (i + 1, 2), "Startfield {} for {} not correct!".format(self.pawns[i].start_field, self.pawns[i].name)
        
        print("Start fields correct!")

    def pawn_movement(self) -> None:
        """
        Tests the movement rules for Pawn objects.

        Validates:
            - A pawn can move two spaces forward from its starting position.
            - A pawn can move one space forward during gameplay.
            - A pawn cannot move two spaces forward after its first move.
            - A pawn cannot move outside the board boundaries.
            - A pawn correctly sets `is_at_end` when reaching the end of the board.
        """

        for i in range(len(self.pawns)):
            test_pawn: Pawn = self.pawns[i]

            test_pawn.move((i + 1,4))
            assert test_pawn.get_Field() == (i + 1,4), "Pawn {} can only move 2 squares at the beginning".format(test_pawn.name)
        
            test_pawn.move((i + 1,5))
            assert test_pawn.get_Field() == (i + 1,5), "Pawn {} cannot move 1 square in the game.".format(test_pawn.name)

            test_pawn.move((i + 1,7))
            assert test_pawn.get_Field() == (i + 1,5), "Pawn {} moves 2 spaces in the game".format(test_pawn.name)

            test_pawn.move((i + 1,6))
            test_pawn.move((i + 1,7))
            test_pawn.move((i + 1,8))
            
            assert test_pawn.is_at_end, "Pawn {} bool does not switch when reaching the end".format(test_pawn.name)

            test_pawn.move((i + 1,9))
            assert test_pawn.get_Field() == (i + 1,8), "Pawn {} can move off the board".format(test_pawn.name)

        print("Move test correct!")
    
    def pawn_attack(self) -> None:
        """
        Placeholder for pawn attack tests.

        Currently, this method only prints a success message.
        """
        
        print("Attack tests correct!")