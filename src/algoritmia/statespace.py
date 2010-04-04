#coding: latin1
from abc import ABCMeta, abstractmethod
from algoritmia.datastructures.queues.lifo import Lifo
from itertools import dropwhile

class IForwardStateSpace(metaclass=ABCMeta): #[forward 
    @abstractmethod
    def initial_states(self) -> "Iterable<State>": pass

    @abstractmethod
    def is_final(self, s: "State") -> "bool": pass

    @abstractmethod
    def decisions(self, s: "State") -> "Iterable<Decision>": pass

    @abstractmethod
    def decide(self, s: "State", d: "Decision") -> "State": pass #]forward

class IReversibleForwardStateSpace(IForwardStateSpace):#[reversible 
    @abstractmethod
    def undo(self, s:"State", d: "Decision") -> "State": pass #]reversible

class IBackwardsStateSpace(metaclass=ABCMeta): #[backwards
    @abstractmethod
    def is_initial(self, s: "State") -> "bool": pass

    @abstractmethod
    def final_states(self) -> "Iterable<State>": pass

    @abstractmethod
    def incoming_decisions(self, s: "State") -> "Iterable<Decision>": pass

    @abstractmethod
    def undo(self, s:"State", d: "Decision") -> "State": pass #]backwards

class StateSpaceTopsorter:#[topsorter #[]topsorter2
    def __init__(self, createLifo: "-> ILifo<(State, Iterable<State>)>"=Lifo,
                       createSet: "-> ISet<State>"=set) -> "Iterable<State>":
        self.createLifo = createLifo
        self.createSet = createSet

    def topsorted(self, space: "StateSpace"):
        if isinstance(space, IBackwardsStateSpace):
            return self._backwards_topsorted(space)
        elif isinstance(space, IForwardStateSpace):
            return reversed(list(self._forward_topsorted(space)))

    def _backwards_topsorted(self, space: "IBackwardsStateSpace"):
        def _postorder_traverse(u: "T"):
            visited.add(u)
            stack.push((u, space.incoming_decisions(u)))
            while len(stack) > 0:
                (v, succs) = stack.pop()
                succs = dropwhile(lambda d: space.undo(v, d) in visited, succs)
                d = next(succs, None)
                if d != None:
                    w = space.undo(v, d)
                    stack.push((v, succs))
                    stack.push((w, space.incoming_decisions(w))) 
                    visited.add(w)
                else:
                    yield v
        visited = self.createSet()
        stack = self.createLifo()
        for s in space.final_states():
            if s not in visited:
                for s_prime in _postorder_traverse(s): 
                    yield s_prime#]topsorter
                    
    def _forward_topsorted(self, space: "IForwardStateSpace"):#[topsorter2
        def _postorder_traverse(u: "T"):
            visited.add(u)
            stack.push((u, space.decisions(u)))
            while len(stack) > 0:
                (v, succs) = stack.pop()
                succs = dropwhile(lambda d: space.decide(v, d) in visited, succs)
                d = next(succs, None)
                if d != None:
                    w = space.decide(v, d)
                    stack.push((v, succs))
                    stack.push((w, space.decisions(w))) 
                    visited.add(w)
                else:
                    yield v
        visited = self.createSet()
        stack = self.createLifo()
        for s in space.initial_states():
            if s not in visited:
                for s_prime in _postorder_traverse(s): 
                    yield s_prime#]topsorter2