#coding: latin1
from algoritmia.statespace import IReversibleForwardStateSpace
from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.problems.perfecthash.basic import PerfectHashStateSpace

#< cichelli
class PerfectHashStateSpace3(IReversibleForwardStateSpace):
    def __init__(self, words, maxvalue):
        freq = {}
        for w in words:
            freq[w[0]] = freq.get(w[0], 0) + 1
            freq[w[-1]] = freq.get(w[-1], 0) + 1
        self.words = sorted(words, key=lambda w: -(freq[w[0]]+freq[w[-1]]))
        self.maxvalue = maxvalue

    class State(PerfectHashStateSpace.State):
        def __init__(self, words):
            super().__init__(words)
            self.found_chars = [set([words[0][0], words[0][-1]])]
            for word in words[1:]:
                self.found_chars.append(set([word[0], word[-1]]) | self.found_chars[-1])
            self.used_values = set()

    def initial_states(self):
        yield PerfectHashStateSpace3.State(self.words)

    def decisions(self, s):
        first, last = self.words[s.i][0], self.words[s.i][-1]

        if first in s.g: first_del, first_from, first_to = False, s.g[first], s.g[first]+1
        else: first_del, first_from, first_to = True, 0, self.maxvalue

        if last in s.g: last_del, last_from, last_to = False, s.g[last], s.g[last]+1
        else: last_del, last_from, last_to = True, 0, self.maxvalue

        for a in range(first_from, first_to):
            for b in range(last_from, last_to):
                v = len(self.words[s.i]) + a + b
                if self.is_promising(s, (a, b, v)):
                    yield a, b, v

    def is_promising(self, s, c_d_v):
        c, d, v = c_d_v
        return v not in s.used_values

    def decide(self, s, c_d_v):
        c, d, v = c_d_v
        s.used_values.add(v)
        s.g[self.words[s.i][0]] = c
        s.g[self.words[s.i][-1]] = d
        s.i += 1
        return s

    def undo(self, s, c_d_v):
        c, d, v = c_d_v
        s.i -= 1
        first, last = self.words[s.i][0], self.words[s.i][-1]
        if first not in s.found_chars[s.i]: del s.g[first]
        if last != first and last not in s.found_chars[s.i]: del s.g[last]
        s.used_values.remove(v)
        return s

    def is_final(self, s):
        return s.i == len(self.words)

    def solution(self, s):
        return lambda w: len(w) + s.g[w[0]] + s.g[w[-1]]

class PerfectHashFinder:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def find(self, words, maxvalue):
        space = PerfectHashStateSpace3(words, maxvalue)
        return next(self.enumerator.enumerate(space))
#> cichelli