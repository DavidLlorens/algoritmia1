#coding: latin1

#< recursive
from algoritmia.utils import infinity

#< greedyscheme2
class ChangeProblem2(ChangeProblem1):
    def __init__(self, v, Q):
        super().__init__(v, Q)

    class State(list):
        def __init__(self):
            super().__init__()
            self.sum = 0

    def initial_states(self):
        yield ChangeProblem2.State()

    def is_final(self, s):
        return len(s) == len(self.v) and s.sum == self.Q

    def decisions(self, s):
        if len(s) < self.n:
            yield (self.Q-s.sum) // self.v[len(s)]

    def destination_is_promising(self, s, d):
        return len(s) < len(self.v) and s.sum + d*self.v[len(s)] <= self.Q

    def take_decision(self, s, d):
        s.sum += d * self.v[len(s)]
        s.append(d)
        return s
#> greedyscheme2

#< greedyscheme3
class ChangeProblem3(ChangeProblem2):
    def __init__(self, v, Q):
        super().__init__(v, Q)

    class State(list):
        def __init__(self, Q):
            super().__init__()
            self.Q = Q

    def initial_states(self):
        yield ChangeProblem3.State(self.Q)

    def is_final(self, s):
        return s.Q == 0 or len(s) == len(self.v)

    def decisions(self, s):
        if len(s) < self.n: yield s.Q // self.v[len(s)]

    def destination_is_promising(self, s, d):
        return len(s) < self.n and s.Q - d*self.v[len(s)] >= 0

    def take_decision(self, s, d):
        s.Q -= d * self.v[len(s)]
        s.append(d)
        return s

    def solution(self, s):
        return s + [0] * (self.n-len(s))
#> greedyscheme3

#< red2
#: snippet[5] = re.sub("\(\(", "(¶(¶", snippet[5])
#: snippet[6] = re.sub("for", "»»for", snippet[6])
#: snippet[7] = re.sub("if", "»if", snippet[7])
#> red2

#< path2
#> path2

#< dp1
class CoinChangeProblem(MinTropicalSemiRing, BackwardDynamicProgrammingProblem):
    def __init__(self, v, w, Q):
        self.v, self.w, self.Q, self.n = v, w, Q, len(v)

    def is_initial(self, qn):
        q, n = qn
        return q==0 and n==0

    def final_states(self):
        yield (self.Q, self.n)

    def incoming_decisions(self, qn):
        q, n = qn
        if n > 0: 
            for i in range(int(q//self.v[n-1])+1): yield i

    def undo_decision(self, qn, d):
        q, n = qn
        return (q-d*self.v[n-1], n-1)

    def weight(self, qn, d):
        q, n = qn
        return d * self.w[n]
#> dp1

#< dp2
class CoinChangeTopSortedProblem(CoinChangeProblem):
    def __init__(self, v, w, Q):
        super().__init__(v, w, Q)

    def topsorted_states(self, digraph_factory=None):
        return ((q, n) for q in range(self.Q+1) for n in range(self.n+1))
#> dp2

#< dp3
class CoinChangeDecisionProblem(MinTropicalBackPointerSemiRing, \
    CoinChangeTopSortedProblem):
    def __init__(self, v, w, Q):
        super().__init__(v, w, Q)

    def weight(self, qn, d):
        q, n = qn
        return ValueWithDecisionAndBackPointer(d * self.w[n], d)
#> dp3

#< dp4
class CoinChangeForwardProblem(CoinChangeTopSortedProblem):
    def __init__(self, v, w, Q):
        super().__init__(v, w, Q)

    def decisions(self, qn):
        q, n = qn
        if n < self.n: 
            for i in range(int((self.Q-q)//self.v[n])+1): yield i

    def take_decision(self, qn, d):
        q, n = qn
        return (q+d*self.v[n], n+1)
#> dp4

#< dp5
class CoinChangeForwardWithMemoryReductionProblem(CoinChangeForwardProblem):
    def __init__(self, v, w, Q):
        super().__init__(v, w, Q)

    def is_final(self, qn):
        q, n = qn
        return q == self.Q and n == self.n
#> dp5

#< dp6
def number_of_coins(Q, v, w, m):
    L = dict(chain([((0,0), 0)], (((q,0), infinity) for q in range(1, Q+1))))
    for n in range(1, len(v)+1):
        for q in range(Q+1):
            L[q,n] = min((L[q-i*v[n-1],n-1] + i * w[n-1]
                         for i in range(min(q//v[n-1]+1, m[n-1]+1))), ifempty=infinity)
    return L[Q,len(v)]
#: snippet[4] = re.sub("\(\(", "(¶(¶", snippet[4])
#: snippet[5] = re.sub("for", "»»for", snippet[5])
#> dp6

#< kbest
class KBestCoinChangeProblem(KMinTropicalSemiRing, BackwardDynamicProgrammingProblem):
    def __init__(self, v, w, Q, k):
        super().__init__(k)
        self.v, self.w, self.Q, self.n = v, w, Q, len(v)

    def is_initial(self, qn):
        q, n= qn
        return q==0 and n==0

    def final_states(self):
        yield (self.Q, self.n)

    def incoming_decisions(self, qn):
        q, n = qn
        if n > 0: 
            for i in range(int(q//self.v[n-1])+1): yield i

    def undo_decision(self, qn, d):
        q, n = qn
        return (q-d*self.v[n-1], n-1)

    def weight(self, qn, d):
        q, n = qn
        return d * self.w[n]

    def topsorted_states(self, digraph_factory=None):
        return ((q, n) for q in range(self.Q+1) for n in range(self.n+1))
#> kbest