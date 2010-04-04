from algoritmia.schemes.backtracking import BacktrackingEnumerator
from algoritmia.problems.perfecthash.basic import PerfectHashStateSpace

class PerfectHashStateSpace2(PerfectHashStateSpace):#[full2
    def __init__(self, words, maxvalue):
        super().__init__(words, maxvalue)

    class State(PerfectHashStateSpace.State):
        def __init__(self, words):
            super().__init__(words)
            freq = {}
            for w in words:
                freq[w[0]] = freq.get(w[0], 0) + 1
                freq[w[-1]] = freq.get(w[-1], 0) + 1
            self.chars.sort(key=lambda char: -freq[char])
            self.available = dict((char, []) for char in self.chars)
            seen_words = set()
            seen_chars = set()
            for char in self.chars:
                seen_chars.add(char)
                for w in words:
                    if w not in seen_words and w[0] in seen_chars and w[-1] in seen_chars:
                        seen_words.add(w)
                        self.available[char].append(w)
            self.used_values = set()

    def initial_states(self):
        yield PerfectHashStateSpace2.State(self.words)


    def decide(self, s, c):
        s.g[s.chars[s.i]] = c
        for w in s.available[s.chars[s.i]]:
            s.used_values.add(len(w) + s.g[w[0]] + s.g[w[-1]])
        s.i += 1
        return s

    def is_promising(self, s, c):
        also_used = set()
        for w in s.available[s.chars[s.i]]:
            a, b = None, None
            if w[0] == s.chars[s.i]: a = c
            elif w[0] in s.g: a = s.g[w[0]]
            if w[-1] == s.chars[s.i]: b = c
            elif w[-1] in s.g: b = s.g[w[-1]]
            if a != None and b != None:
                h = len(w) + a + b
                if h in s.used_values or h in also_used: return False
                also_used.add(h)
        return True

    def undo(self, s, c):
        s.i -= 1
        for w in s.available[s.chars[s.i]]:
            s.used_values.remove(len(w) + s.g[w[0]] + s.g[w[-1]])
        del s.g[s.chars[s.i]]
        return s

class PerfectHashFinder:
    def __init__(self):
        self.enumerator = BacktrackingEnumerator(createSolution=lambda space, i, d, f: f)
    
    def find(self, words, maxvalue):
        space = PerfectHashStateSpace2(words, maxvalue)
        return next(self.enumerator.enumerate(space))#]full2
