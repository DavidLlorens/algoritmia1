#coding: latin1

#< rec
class RecursiveGreedySolver:
    def __init__(self, createList: "-> IList<Decision>"=list,
            createSolution: "(IForwardStateSpace, (IList<Decisions>, State) -> Solution"
                = lambda space, decisions, state: (tuple(decisions), state),
            decisionSelector: "(IForwardStateSpace, State) -> Decision"
                = lambda space, state: next(space.decisions(state))):
        self.createList = createList
        self.createSolution = createSolution
        self.decisionSelector = decisionSelector

    def solve(self, space: "IForwardStateSpace") -> "Solution or None":
        def solve_recursively(self, state: "State"):
            if space.is_final(state): 
                return self.createSolution(self.space, initial, decisions, state)
            d = self.decisionSelector(space, state)
            decisions.append(d)
            return self.solve_recursively(space.decide(state, d))

        initial = next(space.initial_states())
        decisions = self.createList()
        for initial in space.initial_states():
            try: 
                solution = self.solve_recursively(initial)
            except StopIteration: 
                pass
            if solution != None: return solution
#> rec
#< iter
class GreedySolver(RecursiveGreedySolver):
    def solve(self, space: "IForwardStateSpace") -> "Solution or None":
        decisions = self.createList()
        for state in space.initial_states():
            try:
                while not space.is_final(state):
                    d = self.decisionSelector(space, state)
                    state = space.decide(state, d)
                    decisions.append(d)
                solution = self.createSolution(space, decisions, state)
            except StopIteration: 
                pass
            if solution != None: return solution
#> iter