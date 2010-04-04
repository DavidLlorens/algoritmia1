from algoritmia.schemes.backtracking import BacktrackingEnumerator #[full
from algoritmia.statespace import IReversibleForwardStateSpace

class PerfectHashStateSpace(IReversibleForwardStateSpace):
    def __init__(self, words, maxvalue):
        self.words = words
        self.maxvalue = maxvalue

    class State:
        def __init__(self, words):
            self.chars = list(set(w[0] for w in words)|set(w[-1] for w in words))
            self.g = {}
            self.i = 0
            
        def __call__(self, w):
            return len(w) + self.g[w[0]] + self.g[w[-1]]

    def initial_states(self):
        yield PerfectHashStateSpace.State(self.words)

    def is_final(self, s):
        return s.i == len(s.chars)

    def decide(self, s, c):
        s.g[s.chars[s.i]] = c
        s.i += 1
        return s

    def undo(self, s, c):
        s.i -= 1
        del s.g[s.chars[s.i]]
        return s

    def decisions(self, s):
        for c in range(self.maxvalue):
            if self.is_promising(s, c):
                yield c

    def is_promising(self, s, c):
        used = set()
        for w in self.words:
            a, b = None, None
            if w[0] == s.chars[s.i]: a = c
            elif w[0] in s.g: a = s.g[w[0]]
            if w[-1] == s.chars[s.i]: b = c
            elif w[-1] in s.g: b = s.g[w[-1]]
            if a != None and b != None:
                h = len(w) + a + b
                if h in used: return False
                used.add(h)
        return True

class PerfectHashFinder:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def find(self, words, maxvalue):
        space = PerfectHashStateSpace(words, maxvalue)
        return next(self.enumerator.enumerate(space)) #]full
