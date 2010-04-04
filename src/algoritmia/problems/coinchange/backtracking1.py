from algoritmia.problems.coinchange.statespace import MoneyChangeForwardStateSpace

class ChangeEnumerator: #[enumerator
    def __init__(self, createList: "-> IList<int>"=list):
        self.createList = createList
        
    def enumerate(self, space: "MoneyChangeForwardStateSpace") -> "Iterable<Tuple<int>>":
        def backtracking(state: "int") -> "Iterable<Tuple<int>>":
            if space.is_final(state): 
                yield tuple(decisions)
            for decision in space.decisions(state):
                decisions.append(decision)
                successor = space.decide(state, decision)
                for result in backtracking(successor): yield result
                decisions.pop()
        decisions = self.createList()
        initial = next(space.initial_states(), None)
        if initial != None:
            for result in backtracking(initial):
                yield result#]enumerator
