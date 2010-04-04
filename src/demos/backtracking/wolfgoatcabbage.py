#coding: latin1

#< full
from algoritmia.problems.puzzles.wolfgoatcabbage import WolfGoatCabbageSolver

solution = WolfGoatCabbageSolver().solve()
shore = [set(["lobo", "cabra", "col"]), set()]
boat = 0
for i in solution:
    a = " ".join(shore[0])
    b = " ".join(shore[1])
    c = "(barquero, {})".format("nada" if i == '' else str(i))
    if boat == 0: a += " " + "barquero"
    else: b += " " + "barquero"
    print("{:>23}|{:^21}|{:<23}".format(a, " ", b))
    if i != "": shore[boat].remove(i)
    if boat == 0:
        a = " ".join(shore[0])
        print("{:>23}|{:^21}|{:<23}".format(a, c + '->', b))
    else:
        b = " ".join(shore[1])
        print("{:>23}|{:^21}|{:<23}".format(a, '<-' + c, b))
    boat = 1 - boat
    if i != "": shore[boat].add(i)
                                                        
a = " ".join(shore[0])
b = " ".join(shore[1])
if boat == 0: 
    a += " " + "barquero"
else: 
    b += " " + "barquero"
print("{:>23}|{:^21}|{:<23}".format(a, " ", b))
#> full