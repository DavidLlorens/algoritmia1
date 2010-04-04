#coding: latin1
from algoritmia.utils import infinity #[]bfo
from algoritmia.datastructures.sets import DummySet #]bfs2



class BfoWithOptimisticPruningProblem(BestFirstOptimizationProblem): #[bfoprune
    def optimistic(self, s):
        raise NotImplementedError

    def priority(self, s):
        raise Exception("Use optimistic instead of priority")

class BfoWithOptimisticPruningSolver(BestFirstOptimizationSolver):
    def __init__(self, problem, 
            openSetFactory=lambda keyvalues: MaxMinIntervalHeapMap(keyvalues),
            visitedSetFactory=lambda initial_states: DummySet()):
        BestFirstOptimizationSolver.__init__(self, problem, openSetFactory, visitedSetFactory)

    def _initialize_search(self):        
        self.open = self.openSetFactory(\
            (s, self.problem.optimistic(s)) for s in self.problem.initial_states())
        self.visited = self.visitedSetFactory(self.problem.initial_states())
        self.opt_final, self.opt_result = None, self.problem.zero 
        
    def _update_current_solution(self, s):
        result = self.problem.solution(s)
        if self.problem.opt(result, self.opt_result) != self.opt_result:
            self.opt_final, self.opt_result = s, result 
            self._optimistic_pruning()
    
    def _optimistic_pruning(self):
        while len(self.open)>0 and \
            self.problem.opt(self.open.worst_value(), self.opt_result)==self.opt_result:
            self.open.extract_worst()
    
    def _add(self, s):
        optimistic_at_s = self.problem.optimistic(s)
        if self.problem.opt(optimistic_at_s, self.opt_result) != self.opt_result:
            self.open[s] = optimistic_at_s
            self.visited.add(s) #]bfoprune

class BfoWithOptimisticAndEarlyPruningProblem(BfoWithOptimisticPruningProblem): #[bfoearly
    def suboptimal_solution(self):
        raise NotImplementedError

class BfoWithOptimisticAndEarlyPruningSolver(BfoWithOptimisticPruningSolver):
    def __init__(self, problem, 
            openSetFactory=lambda keyvalues: MaxMinIntervalHeapMap(keyvalues),
            visitedSetFactory=lambda initial_states: DummySet()):
        BfoWithOptimisticPruningSolver.__init__(self, problem, openSetFactory, visitedSetFactory)

    def _initialize_search(self):
        BfoWithOptimisticPruningSolver._initialize_search(self)
        self.opt_final = self.problem.suboptimal_solution()
        if self.opt_final != None: 
            self.opt_result = self.problem.solution(self.opt_final)
            self._optimistic_pruning() #]bfoearly

class BfoWithOptimisticImplicitAndEarlyPruningSolver(BfoWithOptimisticAndEarlyPruningSolver): #[bfoimpl
    def __init__(self, problem, 
            openSetFactory=lambda keyvalues: MaxMinIntervalHeapMap(keyvalues),
            visitedSetFactory=lambda initial_states: DummySet(),
            explicit_pruning=False):
        BfoWithOptimisticAndEarlyPruningSolver.__init__(self, \
            problem, openSetFactory, visitedSetFactory)
        self.explicit_pruning = explicit_pruning

    def _there_are_promising_open_states(self):
        return len(self.open)>0 and \
            self.problem.opt(self.open.opt_value(), self.opt_result)!=self.opt_result

    def _optimistic_pruning(self):
        if self.explicit_pruning:
            while len(self.open) > 0 and \
                self.problem.opt(self.open.worst_value(), self.opt_result) == self.opt_result:
                self.open.extract_worst() #]bfoimpl

class BranchAndBoundProblem(BfoWithOptimisticAndEarlyPruningProblem): #[bfopess
    def pessimistic(self, s):
        return self.zero

    one = infinity

class BranchAndBoundSolver(BfoWithOptimisticImplicitAndEarlyPruningSolver):
    def __init__(self, problem, 
            openSetFactory=lambda keyvalues: MaxMinIntervalHeapMap(keyvalues),
            visitedSetFactory=lambda initial_states: DummySet(),
            explicit_pruning=False):
        BfoWithOptimisticImplicitAndEarlyPruningSolver.__init__(\
            self, problem, openSetFactory, visitedSetFactory, explicit_pruning)

    def _initialize_search(self):
        BfoWithOptimisticImplicitAndEarlyPruningSolver._initialize_search(self)
        self.bpe = self.problem.zero
        for s in self.problem.initial_states():
            self.bpe = self.problem.opt(self.bpe, self.problem.pessimistic(s))

    def _add(self, s):
        optimistic_at_s = self.problem.optimistic(s)
        if self.problem.opt(optimistic_at_s, self.opt_result) != self.opt_result and \
            (self.problem.opt(optimistic_at_s, self.bpe) != self.bpe
             or optimistic_at_s == self.bpe):
            self.open[s] = optimistic_at_s
            self.visited.add(s)

    def _optimistic_pruning(self):
        if self.explicit_pruning:
            while len(self.open) > 0 and \
                (self.problem.opt(self.open.worst_value(), self.opt_result) == self.opt_result or
                 (self.problem.opt(self.open.worst_value(), self.bpe) == self.bpe and
                  self.open.worst_value() != self.bpe)):
                 self.open.extract_worst() #]bfopess

class BranchAndBoundWithLimitedMemorySolver(BranchAndBoundSolver): #[bfomem
    def __init__(self, problem,
            openSetFactory=lambda keyvalues: MaxMinIntervalHeapMap(keyvalues),
            visitedSetFactory=lambda initial_states: DummySet(),
            explicit_pruning=False,
            max_states=infinity):
        BranchAndBoundSolver.__init__(self, problem, openSetFactory, visitedSetFactory, explicit_pruning)
        self.max_states = max_states
    
    def _add(self, s):
        if s not in self.visited:
            opt_est = self.problem.optimistic(s)
            if self.problem.opt(opt_est, self.opt_result) != self.opt_result and \
                self.problem.opt(opt_est, self.bpe) != self.bpe:
                if len(self.open) == self.max_states:
                    if self.problem.opt(self.open.worst_value(), opt_est) == opt_est:
                        self.extract_worst()
                        self.open[s] = opt_est
                else:
                    self.open[s] = opt_est
            self.visited.add(s) #]bfomem

class ApproximateBranchAndBoundProblem(BranchAndBoundProblem): #[bfapprox
    def tolerance(self, value):
        return value
    
class ApproximateBranchAndBound(BranchAndBoundWithLimitedMemorySolver):
    def __init__(self, problem,
            openSetFactory=lambda keyvalues: MaxMinIntervalHeapMap(keyvalues),
            closedSetFactory=lambda initial_states: DummySet(),
            explicit_pruning=False,
            max_states=infinity):
        BranchAndBoundWithLimitedMemorySolver.__init__(self, problem, openSetFactory, closed)
        
    def _update_current_solution(self, s):
        result = self.problem.tolerance(self.problem.solution(s))
        if self.problem.opt(result, self.opt_result) != self.opt_result:
            self.opt_final, self.opt_result = s, result
            self._optimistic_pruning() #]bfapprox

#< bfdijkstra
#class NonNegativeSemiRingBranchAndBoundProblem(SemiRing, BfoWithOptimisticAndEarlyPruningProblem):
#    def pessimistic(self, s):
#        return self.one
#
#    one = infinity
#    
#class NonNegativeSemiRingBranchAndBoundSolver:
#    def __init__(self, problem, 
#            openSetFactory=lambda problem: \
#                PriorityDict(opt=problem.plus, (s, self.problem.optimistic(s)) for s in self.problem.initial_states()),
#            scoreDictFactory=lambda: dict(),
#            backDictFactory=lambda: dict()):
#        self.problem = problem
#        self.openSetFactory = openSetFactory
#        self.scoreDictFactory = scoreDictFactory
#        self.backDictFactory = backDictFactory
#        
#    def _initialize_search(self):
#        self.open = self.openSetFactory(self.problem)
#        self.optimistic_completion = self.scoreDictFactory()
#        self.mem = self.scoreDictFactory()
#        self.back = self.backDictFactory()
#        for s in self.problem.initial_states(): 
#            self.mem[s] = self.problem.one
#            self.back[s] = (None, None)
#
#    def _add_from(self, s_prime, d, s):
#        if s not in self.optimistic_completion:
#            self.optimistic_completion[s] = self.problem.optimistic_completion(s)
#        known_score = self.times(self.mem[s_prime], self.problem.weight(s_prime, d))
#        optimistic_estimation = self.problem.plus(known_score, self.optimistic_completion[s])
#        if self.problem.opt(optimistic_estimation, self.opt_result) != self.opt_result:
#            if s in self.open:
#                best = self.problem.plus(self.open[s], optimistic_estimation)
#                if best != self.open[s]:
#                    self.mem[s] = known_score
#                    self.back[s] = (s_prime, s)
#                    self.open[s] = self.problem.plus(self.open[s], optimistic_estimation)
#            else:
#                self.mem[s] = known_score
#                self.back[s] = (s_prime, s)
#                self.open[s] = self.problem.plus(self.open[s], optimistic_estimation)
#                
#    def solve(self):
#        self._initialize_search()
#        while self._there_are_promising_open_states():
#            s = self.open.extract_opt()
#            if self.problem.is_final(s):
#                self._update_current_solution(s)
#            for d in self.decisions(s):
#                if self._destination_is_promising(s, d):
#                    s_prime = self.problem.take_decision(s, d)
#                    self._add_from(s_prime, d, s)
#        return self.opt_final, self.opt_result
#> bfdijkstra