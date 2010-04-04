#coding: latin1

#< full
from algoritmia.datastructures.prioritymaps import MaxHeapMap

def dHondt_law(votes, m):
    Q = MaxHeapMap(((party, (votes[party], 1)) for party in votes))
    result = []
    for i in range(m):
        (party, (rest, j)) = Q.opt_item()
        result.append(party)
        Q[party] = (votes[party]/(j+1), j+1)
    return result

if __name__ == "__main__":
    print(dHondt_law({'PA': 60, 'PB': 100, 'PC': 40, 'PD': 10, 'PE': 5}, 4))
#> full