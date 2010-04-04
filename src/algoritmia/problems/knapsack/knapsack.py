#coding: latin1
#< bb1
from algoritmia.datastructures.priorityqueues import MaxHeap
from algoritmia.utils import infinity
from collections import namedtuple
#> bb1
#< bb3
from algoritmia.datastructures.doubleendedprioritymaps import MaxMinIntervalHeapMap
from fractions import  Fraction
#> bb3

#< bb1
def branch_and_bound_knapsack0(v, w, W):
    Item = namedtuple("Item", "score knownvalue knownweight x")
    N = len(v)
    xhat, fxhat = None, -infinity
    A = MaxHeap([Item(sum(v), 0, 0, tuple())])
    while len(A) > 0:
        s = A.extract_opt()
        for d in (0, 1):
            x = s.x + (d,)
            knownweight = s.knownweight + d * w[len(x)-1]
            knownvalue = s.knownvalue + d * v[len(x)-1]
            if len(x) == N:
                if knownweight <= W and knownvalue > fxhat:
                    xhat, fxhat = x, knownvalue
            else:
                weight, score = knownweight, knownvalue
                for i in range(len(x), N):
                    if weight + w[i] <= W:
                        weight += w[i]
                        score += v[i]
                if knownweight <= W:
                    A.add(Item(score, knownvalue, knownweight, x))
    return xhat, fxhat
#> bb1

#< bb2
def branch_and_bound_knapsack1(v, w, W):
    Item = namedtuple("Item", "score knownvalue knownweight x")
    A = MaxHeap([Item(sum(v), 0, 0, tuple())])
    N = len(v)
    xhat, fxhat = None, -infinity
    while len(A) > 0:
        s = A.extract_opt()
        for d in (0, 1):
            x = s.x + (d,)
            knownweight = s.knownweight + d * w[len(x)-1]
            knownvalue = s.knownvalue + d * v[len(x)-1]
            if len(x) == N:
                if knownweight <= W and knownvalue > fxhat:
                    xhat, fxhat = x, knownvalue
            else:
                score = knownvalue + sum(v[len(x):])
                A.add(Item(score, knownvalue, knownweight, x))
    return xhat, fxhat
#> bb2

#< bb3
def fractional_knapsack_profit(v, w, W):
    W = Fraction(W, 1)
    x = [0] * len(w)
    for i in reversed(sorted(range(len(w)), key=lambda i: Fraction(v[i], w[i]))):
        x[i] = min(1, W / w[i])
        W -= x[i] * w[i]
    return sum(x[i] * v[i] for i in range(len(w)))

def branch_and_bound_knapsack3(v, w, W):
    Item = namedtuple("Item", "score knownvalue x")
    N = len(v)
    A = MaxMinIntervalHeapMap((\
        ((0,c), Item(fractional_knapsack_profit(v, w, W-c), 0, tuple())) for c in range(W+1)))
    xhat, fxhat = None, -infinity
    while len(A) > 0:
        (n, c), item = A.extract_opt_item()
        for d in (0, 1):
            x = item.x + (d,)
            knownvalue = item.knownvalue + d * v[n]
            if n+1 == N:
                if c + d * w[n] <= W and knownvalue > fxhat:
                    xhat, fxhat = x, knownvalue
                    while len(A) > 0 and A.worst_value().score <= fxhat: A.extract_min()
            elif c + d * w[n] <= W:
                (n_prime, c_prime) = (n + 1, c + d * w[n]) 
                score = knownvalue + fractional_knapsack_profit(v[n_prime:],w[n_prime:],W-c_prime)
                if (n_prime, c_prime) in A:
                    if A[n_prime, c_prime].score < score:
                        A[n_prime, c_prime] = Item(score, knownvalue, x)
                else:
                    A[n_prime, c_prime] = Item(score, knownvalue, x)
    return xhat, fxhat
#> bb3

#< bb4
class KnapsackAsBestFirstSearchProblem:
    class State:
        def __init__(self, state=None, decision=None, v=None, w=None):
            self.parent = state
            self.decision = decision
            self.vsum = state.vsum + decision * v[state.len] if state != None else 0
            self.wsum = state.wsum + decision * w[state.len] if state != None else 0
            self.len = state.len + 1 if state != None else 0 
            
        def decision_sequence(self):
            ds = []
            p = self
            while p.parent != None:
                ds.append(p.decision)
                p = p.parent
            return tuple(reversed(ds))
            
        def __repr__(self):
            return str(self.decision_sequence())
        
        def __len__(self):
            return self.len
        
        def __getitem__(self, i):
            if i < 0 or i >= self.len: raise IndexError
            if self.len-1 == i: return self.decision
            return self.parent[i]

    def __init__(self, v, w, W):
        self.v, self.w, self.W, self.n = v, w, W, len(v)
        
    def initial_states(self):
        yield KnapsackAsBestFirstSearchProblem.State(v=self.v, w=self.w)

    def is_final(self, s):
        return s.wsum <= self.W and s.len == self.n

    def decisions(self, s):
        if s.len < self.n:
            yield 1
            yield 0

    def take_decision(self, s, d):
        return KnapsackAsBestFirstSearchProblem.State(s, d, self.v, self.w)

    def destination_is_promising(self, s, d):
        return s.wsum + d * self.w[s.len] <= self.W

    def priority(self, s):
        return s.vsum
        
    def solution(self, s):
        return s.vsum
#> bb4

#< bb5
class KnapsackAsBestFirstOptimizationProblem(KnapsackAsBestFirstSearchProblem):
    def __init__(self, v, w, W):
        super().__init__(v, w, W)
    
    def solution(self, s):
        return sum(s[i]*self.v[i] for i in range(len(s)))
    
    def opt(self, a, b):
        return max(a, b)

    zero = -infinity
#> bb5

#< bb6
class KnapsackAsBfoWithOptimisticPruningProblem(KnapsackAsBestFirstOptimizationProblem):
    def __init__(self, v, w, W):
        super().__init__(v, w, W)
        self.vrestsum = [0] * (self.n+1)
        for i in range(self.n-1, -1, -1):
            self.vrestsum[i] = self.vrestsum[i+1] + self.v[i]
    
    def optimistic(self, s):
        return s.vsum + self.vrestsum[s.len]
#> bb6

#< bb7
class KnapsackAsBfoWithOptimisticPruningProblem2(KnapsackAsBestFirstOptimizationProblem):
    def __init__(self, v, w, W):
        super().__init__(v, w, W)
    
    def optimistic(self, s):
        W = Fraction(self.W-s.wsum)
        v = self.v[s.len:]
        w = self.w[s.len:]
        vsum = s.vsum
        for i in reversed(sorted(range(len(w)), key=lambda i: v[i]/float(w[i]))):
            xi = min(1, W / w[i])
            W -= xi * w[i]
            vsum += xi * v[i]
        return float(vsum)
#> bb7

#< bb8
class KnapsackBfoWithOptimisticAndEarlyPruningProblem(KnapsackAsBfoWithOptimisticPruningProblem2):
    def __init__(self, v, w, W):
        super().__init__(v, w, W)
    
    def suboptimal_solution(self):
        W = self.W
        x = [0] * self.n
        for i in reversed(sorted(range(self.n), key=lambda i: self.v[i]/float(self.w[i]))):
            if self.w[i] < W:
                x[i] = 1
                W -= x[i] * self.w[i]
        return tuple(x) 
#> bb8

#< bb10
class KnapsackAsBranchAndBoundProblem(KnapsackBfoWithOptimisticAndEarlyPruningProblem):
    def __init__(self, v, w, W):
        super().__init__(v, w, W)
    
    def pessimistic(self, s):
        W = self.W-s.wsum
        v = self.v[s.len:]
        w = self.w[s.len:]
        vsum = s.vsum
        for i in reversed(sorted(range(len(w)), key=lambda i: v[i]/float(w[i]))):
            if w[i] <= W:
                W -= w[i]
                vsum += v[i]
        return vsum
#> bb10