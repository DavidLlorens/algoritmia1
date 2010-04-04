class ChangeEnumerator: #[enumerator
    def __init__(self, createList: "-> IList<int>"=list,
                 createSet: "-> ISet<(int, int)>"=set):
        self.createList = createList
        self.createSet = createSet
        
    def enumerate(self, space: "MoneyChangeStateSpace") -> "Iterable<Tuple<int>>":
        def backtracking(state: "int") -> "Iterable<Tuple<int>>":
            if space.is_final(state): 
                yield tuple(decisions)
            seen.add(state)
            for decision in space.decisions(state):
                decisions.append(decision)
                successor = space.decide(state, decision)
                if successor not in seen:
                    for result in backtracking(successor): 
                        yield result
                decisions.pop()
        decisions = self.createList()
        seen = self.createSet()
        initial = next(space.initial_states(), None)
        if initial != None:
            for result in backtracking(initial):
                yield result
    
    def first(self, space: "MoneyChangeStateSpace") -> "Tuple<int>":
        return next(self.enumerate(space), None)#]enumerator