#coding: latin1
from algoritmia.problems.knapsack import *
from algoritmia.schemes.branchandbound import *
from algoritmia.utils import infinity
from algoritmia.datastructures.prioritydicts import PriorityDict
from algoritmia.datastructures.sets import DummySet
from random import seed, randrange

calls = {}
asize = 0

def count(func):
    def wrapper(*args):
        calls[func.__name__] = calls.get(func.__name__, 0) + 1
        return func(*args)
    return wrapper

def logsize(func):
    def wrapper(*args):
        global asize
        asize = max(len(args[0].open), asize)
        return func(*args)
    return wrapper


class ProfiledBestFirstSearchSolver(BestFirstSearchSolver):
    def __init__(self, problem, 
            priorityDictFactory=lambda keyvalues: PriorityDict(keyvalues),
            stateSetFactory=lambda initial_states: DummySet()):
        BestFirstSearchSolver.__init__(self, problem, priorityDictFactory, stateSetFactory)
    
    _initialize_search = count(BestFirstSearchSolver._initialize_search)
    _there_are_promising_open_states = logsize(count(BestFirstSearchSolver._there_are_promising_open_states))
    _branch = count(BestFirstSearchSolver._branch)
    _add = count(BestFirstSearchSolver._add)
        
class ProfiledBestFirstOptimizationSolver(BestFirstOptimizationSolver):
    def __init__(self, problem, 
            priorityDictFactory=lambda keyvalues: PriorityDict(keyvalues),
            stateSetFactory=lambda initial_states: DummySet()):
        BestFirstOptimizationSolver.__init__(self, problem, priorityDictFactory, stateSetFactory)

    _initialize_search = count(BestFirstOptimizationSolver._initialize_search)
    _there_are_promising_open_states = count(BestFirstOptimizationSolver._there_are_promising_open_states)
    _branch = count(BestFirstOptimizationSolver._branch)
    _add = count(BestFirstOptimizationSolver._add)

class ProfiledBfoWithOptimisticPruningSolver(BfoWithOptimisticPruningSolver):
    def __init__(self, problem, 
            doubleEndedPriorityDictFactory=lambda keyvalues: MaxMinPriorityDict(keyvalues),
            stateSetFactory=lambda initial_states: DummySet()):
        BfoWithOptimisticPruningSolver.__init__(self, problem, doubleEndedPriorityDictFactory, stateSetFactory)

    _initialize_search = count(BfoWithOptimisticPruningSolver._initialize_search)
    _there_are_promising_open_states = count(BfoWithOptimisticPruningSolver._there_are_promising_open_states)
    _branch = count(BfoWithOptimisticPruningSolver._branch)
    _add = count(BfoWithOptimisticPruningSolver._add)
    _update_current_solution = count(BfoWithOptimisticPruningSolver._update_current_solution)
    _optimistic_pruning = count(BfoWithOptimisticPruningSolver._optimistic_pruning)
    
    
class ProfiledBfoWithOptimisticAndEarlyPruningSolver(BfoWithOptimisticAndEarlyPruningSolver):
    def __init__(self, problem, 
            doubleEndedPriorityDictFactory=lambda keyvalues: MaxMinPriorityDict(keyvalues),
            stateSetFactory=lambda initial_states: DummySet()):
        BfoWithOptimisticAndEarlyPruningSolver.__init__(self, problem, doubleEndedPriorityDictFactory, stateSetFactory)

    _initialize_search = count(BfoWithOptimisticAndEarlyPruningSolver._initialize_search)
    _there_are_promising_open_states = count(BfoWithOptimisticAndEarlyPruningSolver._there_are_promising_open_states)
    _branch = count(BfoWithOptimisticAndEarlyPruningSolver._branch)
    _add = count(BfoWithOptimisticAndEarlyPruningSolver._add)
    _update_current_solution = count(BfoWithOptimisticAndEarlyPruningSolver._update_current_solution)
    _optimistic_pruning = count(BfoWithOptimisticAndEarlyPruningSolver._optimistic_pruning)

class ProfiledBfoWithOptimisticImplicitAndEarlyPruningSolver(BfoWithOptimisticImplicitAndEarlyPruningSolver):
    def __init__(self, problem, 
            doubleEndedPriorityDictFactory=lambda keyvalues: MaxMinPriorityDict(keyvalues),
            stateSetFactory=lambda initial_states: DummySet(),
            explicit_pruning=False):
        BfoWithOptimisticImplicitAndEarlyPruningSolver.__init__(self, problem, doubleEndedPriorityDictFactory, stateSetFactory)
        
    _initialize_search = count(BfoWithOptimisticImplicitAndEarlyPruningSolver._initialize_search)
    _there_are_promising_open_states = count(BfoWithOptimisticImplicitAndEarlyPruningSolver._there_are_promising_open_states)
    _branch = count(BfoWithOptimisticImplicitAndEarlyPruningSolver._branch)
    _add = count(BfoWithOptimisticImplicitAndEarlyPruningSolver._add)
    _update_current_solution = count(BfoWithOptimisticImplicitAndEarlyPruningSolver._update_current_solution)
    _optimistic_pruning = count(BfoWithOptimisticImplicitAndEarlyPruningSolver._optimistic_pruning)

class ProfiledBranchAndBoundProblem(BranchAndBoundSolver):
    def __init__(self, problem, 
        doubleEndedPriorityDictFactory=lambda keyvalues: MaxMinPriorityDict(keyvalues),
        stateSetFactory=lambda initial_states: DummySet(),
        explicit_pruning=False):
        BranchAndBoundSolver.__init__(self, problem, doubleEndedPriorityDictFactory, stateSetFactory)
    
    _initialize_search = count(BranchAndBoundSolver._initialize_search)
    _there_are_promising_open_states = count(BranchAndBoundSolver._there_are_promising_open_states)
    _branch = count(BranchAndBoundSolver._branch)
    _add = count(BranchAndBoundSolver._add)
    _update_current_solution = count(BranchAndBoundSolver._update_current_solution)
    _optimistic_pruning = count(BranchAndBoundSolver._optimistic_pruning)
    
seed(0)

desde = 1
hasta = 13
incr = 1
limites = [13, 13, 13, 0, 0, 0, 0] # A partir de ahí nada.
repeticiones = 10
resultados = {}
for N in range(desde, hasta, incr):
    resultados[N] = {}
    for rep in range(repeticiones):
        v = [randrange(100) for i in range(N)]
        w = [1+randrange(100) for i in range(N)]
        x = [(0 if randrange(122) else 1) for i in range(N)]
        W = sum(x[i]*w[i] for i in range(N))
        fsolution = None
        
        if N < limites[0]:
            asize = 0
            calls = {}
            problem = KnapsackAsBestFirstSearchProblem(v, w, W)
            solver = ProfiledBestFirstSearchSolver(problem)
            x, fx = None, -infinity
            for solution in solver.solve_all():
                fsolution = sum(solution[i]*v[i] for i in range(len(solution)))
                if fsolution > fx: x, fx = solution, fsolution
            for k, val in calls.items():
                resultados[N][(0, k)] = resultados[N].get((0, k), 0) + val
            resultados[N][(0, 'open')] = asize
        
        for j, (PRB, SLV) in enumerate([
                         (KnapsackAsBestFirstOptimizationProblem,  ProfiledBestFirstOptimizationSolver),
                         (KnapsackAsBfoWithOptimisticPruningProblem, ProfiledBfoWithOptimisticPruningSolver),
                         (KnapsackAsBfoWithOptimisticPruningProblem2, ProfiledBfoWithOptimisticPruningSolver),
                         (KnapsackBfoWithOptimisticAndEarlyPruningProblem, ProfiledBfoWithOptimisticAndEarlyPruningSolver),
                         (KnapsackBfoWithOptimisticAndEarlyPruningProblem, ProfiledBfoWithOptimisticImplicitAndEarlyPruningSolver),
                         (KnapsackAsBranchAndBoundProblem, ProfiledBranchAndBoundProblem),
                         ]):
            if N < limites[j+1]:
                calls = {}
                problem = PRB(v, w, W)
                x = SLV(problem).solve()
                if fsolution != None:
                    assert sum(x[i]*v[i] for i in range(len(x))) == fsolution
                else:
                    fsolution = sum(x[i]*v[i] for i in range(len(x)))
                for k, val in calls.items():
                    resultados[N][(j+1, k)] = resultados[N].get((j+1, k), 0) + val


tr = {}
tr['_add']                               = "Inserciones           "
tr['_there_are_promising_open_states'] = "Iteraciones           "
tr['_update_current_solution']           = "Actualizaciones de $x$"
tr['open']           = "Máxima talla del conjunto de estados activos"
S = set()
for k in resultados:
    for kk in resultados[k]:
        S.add(kk[0])
S = list(sorted(S))

alg = ['BFS', 'BFO', '']
for f in '_there_are_promising_open_states', '_add', '_update_current_solution', 'open':
    print(r"\begin{{tabular}}{{{}}}".format('r' * ((hasta-desde)/incr+1)))
    print("  &", end=' ')
    for n in range(desde, hasta, incr):
        if n < hasta-incr: print("{:8} &".format(n), end=' ')
        else: print(r"{:8} \\".format(n))
    for j in S:
        print(r'{} &'.format(j), end=' ')
        for n in range(desde, hasta, incr):
            if n < hasta-incr: amp = '&'
            else: amp = r'\\'
            if (j, f) in resultados[n]:
                if f == 'open':
                    v = '%8d' % (resultados[n][(j,f)])                
                else:
                    v = '%8.2f' % (resultados[n][(j,f)]/float(repeticiones))
            else: v = '     ---' 
            if amp == '&': print('{} {}'.format(v, amp), end=' ')
            else: print('{} {}'.format((v, amp)))
    print(r"\end{tabular}")
    print(r"\begin{{caption}}{}\end{{caption}}".format(tr[f]))
    print()

print(asize)
print("FIN")