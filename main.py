from MyPawn import Pawn

pawn_01 = Pawn("Pawn01", (1,2))
pawn_02 = Pawn("Pawn02", (2,2))
pawn_03 = Pawn("Pawn03", (3,2))
pawn_04 = Pawn("Pawn04", (4,2))
pawn_05 = Pawn("Pawn05", (5,2))
pawn_06 = Pawn("Pawn06", (6,2))
pawn_07 = Pawn("Pawn07", (7,2))
pawn_08 = Pawn("Pawn08", (8,2))

pawns: Pawn = [pawn_01, pawn_02, pawn_03, pawn_04, pawn_05, pawn_06, pawn_07, pawn_08]

print(pawns[0].current_field)
pawns[0].move((1,3))
print(pawns[0].current_field)
pawns[0].move((1,4))
print(pawns[0].current_field)
pawns[0].move((1,5))
print(pawns[0].current_field)
pawns[0].move((1,6))
print(pawns[0].current_field)
pawns[0].move((1,7))
print(pawns[0].current_field)
pawns[0].move((1,8))
print(pawns[0].current_field)
pawns[0].move((1,9))
pawns[0].move((1,10))
print(pawns[0].current_field)