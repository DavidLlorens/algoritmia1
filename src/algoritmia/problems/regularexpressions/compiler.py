#coding: latin1
from algoritmia.datastructures.queues.lifo import Lifo
from algoritmia.datastructures.queues.fifo import Fifo

class RegularExpressionParser: #[parser
    def __init__(self, createLifo: "-> ILifo"=lambda: Lifo()):
        self.createLifo = createLifo

    def tokenize(self, expression: "str") -> "Iterable<str>":
        p = None
        for c in expression.replace(" ", ""):
            if p not in [None, "(", "|"] and c not in [")", "|", "*"]:
                yield "·"
            yield c
            p = c

    def parse(self, expression: "str") -> "ITree<str>":
        S = self.createLifo()
        tree = []
        op = {'|': 0, '·': 1}
        for token in self.tokenize(expression):
            if token not in "·|*()":
                tree.append([token])
            elif token in op:
                while len(S) > 0 and S.top() in op and op[token] <= op[S.top()]:
                    tree[-2:] = [[S.pop(), tree[-2], tree[-1]]]
                S.push(token)
            elif token == '*':
                tree[-1:] = [["*", tree[-1]]]
            elif token == '(':
                S.push('(')
            elif token == ')':
                while S.top() != '(':
                    tree[-2:] = [[S.pop(), tree[-2], tree[-1]]]
                S.pop()
        while len(S) > 0:
            tree[-2:] = [[S.pop(), tree[-2], tree[-1]]]
        return tree[0] #]parser

class NfaSet: #[thompson
    def __init__(self):
        self.cnt = 0
        self.t = {}
    
    class Nfa:
        def __init__(self, nfa_set: "NfaSet",  start: "int"=None, end: "int"=None):
            self.nfa_set = nfa_set
            self.start = self.add_state() if start == None else start
            self.end = self.add_state() if end == None else end
        
        def add_state(self):
            return self.nfa_set.add_state()
        
        def add_transition(self, tail: "int", symbol: "str", head: "int"):
            self.nfa_set.add_transition(tail, symbol, head)

        def destinations(self, q: "int", c: "str") -> "Iterable<int>":
            if q in self.nfa_set.t and c in self.nfa_set.t[q]:
                for r in self.nfa_set.t[q][c]: yield r

        def output_symbols(self, q: "int") -> "Iterable<str>":
            if q in self.nfa_set.t:
                for c in self.nfa_set.t[q]:
                    yield c
                
        def concat(self, other: "Nfa") -> "Nfa":
            a = self.nfa_set.create_nfa(self.start, other.end)
            self.add_transition(self.end, None, other.start)
            return a
        
        def union(self, other: "Nfa") -> "Nfa":   
            a = self.nfa_set.create_nfa()
            self.add_transition(a.start, None, self.start)
            self.add_transition(a.start, None, other.start)
            self.add_transition(self.end, None, a.end)
            self.add_transition(other.end, None, a.end)
            return a
            
        def close(self) -> "Nfa":
            a = self.nfa_set.create_nfa()
            self.add_transition(a.start, None, self.start)
            self.add_transition(self.end, None, a.start)
            self.add_transition(a.start, None, a.end)
            return a
        
        def __str__(self) -> "str":
            s = []
            s.append('Start: {}'.format(self.start))
            s.append('Final: {}'.format(self.end))
            for k in sorted(self._reachable(self.start)):
                for c in sorted(self.nfa_set.t[k]):
                    s.append("{}, {} -> {}".format(k, c, self.nfa_set.t[k][c]))
            return '\n'.join(s)

        def _reachable(self, q: "int", states: "ISet<int> or None"=None) -> "Iterable<int>":
            if states == None: states = set()
            states.add(q)
            for c in self.nfa_set.t[q]:
                for r  in self.nfa_set.t[q][c]:
                    if r not in states:
                        self._reachable(r, states)
            return states
    
    def create_nfa(self, start: "int"=None, end: "int"=None) -> "Nfa":
        return NfaSet.Nfa(self, start, end)
    
    def add_state(self) -> "int":
        self.cnt += 1
        self.t[self.cnt-1] = {}
        return self.cnt-1
    
    def add_transition(self, tail: "int", symbol: "str", head: "int"):
        if symbol not in self.t[tail]: self.t[tail][symbol] = []
        self.t[tail][symbol].append(head)

class ThompsonAutomatonBuilder:
    def build(self, tree: "regex tree") -> "Nfa":
        self.nfa_set = NfaSet()
        return self._build(tree)
    
    def _build(self, t: "regex tree") -> "Nfa":
        if t[0] == '*':
            return self._build(t[1]).close()
        elif t[0] == "·":
            return self._build(t[1]).concat(self._build(t[2]))
        elif t[0] == "|":
            return self._build(t[1]).union(self._build(t[2]))
        else:
            a = self.nfa_set.create_nfa()
            a.add_transition(a.start, t[0], a.end)
            return a#]thompson

class DFA:
    def __init__(self):
        self.Q = set()
        self.t = dict()
        self.F = set()
        
    def add_state(self, q):
        self.Q.add(q)
    
    def start(self, q):
        self.s = q
    
    def final(self, q):
        self.F.add(q)
        
    def add_transition(self, head, symbol, tail):
        if not head in self.t:
            self.t[head] = {}
        self.t[head][symbol] = tail
        
    def destination(self, q, symbol):
        if q in self.t:
            if symbol in self.t[q]:
                return self.t[q][symbol]
        return None

    def __str__(self) -> "str":
        s = []
        s.append('Start: {}'.format(self.s))
        s.append('Finals: {}'.format(self.F))
        for q in sorted(self.Q):
            if q in self.t:
                for c in self.t[q]:
                    s.append("{}, {} -> {}".format(q, c, self.t[q][c]))
        return '\n'.join(s)
    
    @staticmethod
    def build_from_NFA(nfa):
        def lambda_closure(qs):
            v = set(qs)
            queue = Fifo(qs)
            while len(queue) > 0:
                q = queue.pop()
                for q_prime in nfa.destinations(q, None):
                    if q_prime not in v:
                        v.add(q_prime)
                        queue.push(q_prime)
            return tuple(sorted(v))
        trans = {}
        q = lambda_closure([nfa.start])
        queue = Fifo([q])
        dfa= DFA()
        q_prime = trans[q] = len(trans)
        dfa.add_state(q_prime)
        dfa.s = q_prime
        if nfa.end in q:
            dfa.final(q_prime)
        while len(queue) > 0:
            q = queue.pop()
            output = set()
            for q_prime in q:
                output.update(nfa.output_symbols(q_prime))
            for c in output:
                if c != None:
                    new_q_from = set()
                    for q_prime in q:
                        new_q_from.update(nfa.destinations(q_prime, c))
                    qq = lambda_closure(new_q_from)
                    if qq not in trans:
                        dfaq = trans[qq] = len(trans)
                        dfa.add_state(dfaq)
                        if nfa.end in qq:
                            dfa.final(dfaq)
                        queue.push(qq)
                    dfa.add_transition(trans[q], c, trans[qq])
        return dfa


    