#coding: latin1
from algoritmia.statespace import IReversibleForwardStateSpace
from algoritmia.datastructures.sets.dummyset import DummySet

class BacktrackingEnumerator: #[solver
    def __init__(self, createList: "-> IList<Decision>"=list,
            createSet: "IForwardStateSpace -> ISet<State>"
                =lambda stateSpace: DummySet(),
            createSolution: "(IForwardStateSpace, (IList<Decisions>, State) -> Solution"
                = lambda space, initial, decisions, final: (initial, tuple(decisions), final)):
        self.createList = createList
        self.createSet = createSet
        self.createSolution = createSolution
        
    def enumerate(self, space: "IForwardStateSpace") -> "Iterable<Solution>":
        def backtracking(state: "State") -> "Iterable<Solution>":
            if space.is_final(state): 
                yield self.createSolution(space, initial, decisions, state)
            seen.add(state)
            for decision in space.decisions(state):
                decisions.append(decision)
                successor = space.decide(state, decision)
                if successor not in seen:
                    for result in backtracking(successor): 
                        yield result
                if reversible:
                    state = space.undo(successor, decision)
                decisions.pop()
        
        reversible = isinstance(space, IReversibleForwardStateSpace)
        decisions = self.createList()
        seen = self.createSet(space)
        for initial in space.initial_states():
            for result in backtracking(initial): 
                yield result
    
    def first(self, space: "IForwardStateSpace") -> "Solution or None":
        return next(self.enumerate(space), None)#]solver
