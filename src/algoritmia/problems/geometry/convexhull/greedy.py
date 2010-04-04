from algoritmia.statespace import IForwardStateSpace
from algoritmia.problems.geometry.utils import Point2D, right
from algoritmia.utils import argmax
from math import atan2
from algoritmia.datastructures.lists.linkedlist import LinkedList
from algoritmia.schemes.greedy import GreedySolver

#< greedy
class ConvexHullSpaceState(IForwardStateSpace):
    def __init__(self, S: "ISet<Point2D>"):
        S = [Point2D(*p) for p in S]
        min_y = min(pt.y for pt in S)
        p = argmax((pt for pt in S if pt.y == min_y), lambda pt: pt.x)
        self.points = [p] + list(sorted((q for q in S if q != p), \
            key=lambda q: (atan2(p.y-q.y, p.x-q.x), q.x)))

    class State:
        def __init__(self, points: "ISet<Point2D>"):
            self.point = LinkedList(points)
            self.front = self.point._head.next.next.next

    def initial_states(self):
        yield ConvexHullSpaceState.State(self.points)

    def is_final(self, s: "State") -> "bool":
        return s.front == None

    def decisions(self, s: "State") -> "Iterable<IList<Point2D>>":
        discarded = []
        node = s.front.prev
        while right(node.prev.value, node.value, s.front.value):
            discarded.append(node)
            node = node.prev
        yield discarded
        
    def decide(self, s: "State", discarded: "IList<Point2D>") -> "State":
        s.front = s.front.next
        for node in discarded: s.point._remove(node)
        return s

class ConvexHullFinder:
    def __init__(self):
        self.solver = GreedySolver(createSolution=lambda space, d, s: list(s.point))
    
    def find(self, S: "ISet<IPoint2D>") -> "Iterable<int>":
        hull = self.solver.solve(ConvexHullSpaceState(S))
        return [S.index(p) for p in hull]
#> greedy
