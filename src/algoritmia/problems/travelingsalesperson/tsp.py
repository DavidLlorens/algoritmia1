#coding: latin1

#< nn
from math import sqrt
from algoritmia.utils import argmin
#> nn
#< mst
from algoritmia.datastructures.graphs import UndirectedGraph 
from algoritmia.problems.minimumspanning import KruskalsMinimumSpanningForestFinder
from algoritmia.problems.traversals import PreorderTraverser
#> mst
#< bb
from algoritmia.utils import infinity
from random import sample
#> bb
#< bb5
from algoritmia.utils import min
#> bb5
#< bb6
from algoritmia.datastructures.graphs import Digraph, WeightingFunction
from algoritmia.problems.positivedigraphshortestpaths import DijkstraWithPriorityDictShortestPaths
#> bb6
#< bb7
from algoritmia.datastructures.prioritymaps import MinHeapMap
#> bb7

#< nn

#> nn

#< mst
    def mst_tsp(points):
        G = UndirectedGraph(E=[(a, b) for a in points for b in points if a!=b])
        MST = UndirectedGraph(V=points, E=KruskalsMinimumSpanningForestFinder().minimum_spanning_forest(G, d))
        path = [ v for v in preorder_traversal(MST, points[0]) ] + [points[0]]
        return path
#> mst


#< bb
class _StateBase:
    def __init__(self, s, v):
        self.parent, self.v = s, v
        self.len = 0 if s == None else s.len + 1

    def cycle(self):
        ds = []
        p = self
        while p != None:
            ds.append(p.v)
            p = p.parent
        ds.append(ds[0])
        return tuple(reversed(ds))
    
    def head(self):
        if self.parent == None: return self.v
        else: return self.parent.head()
    
    def visited(self):
        if self.parent == None: return set([self.v])
        nodes = self.parent.visited()
        nodes.add(self.v)
        return nodes
    
    def __repr__(self):
        return str(self.cycle())

    def __getitem__(self, i):
        if i < 0 or i >= self.len: raise IndexError
        if self.len-1 == i: return self.v
        return self.parent[i]

    def __len__(self):
        return self.len

class TspAsBranchAndBoundProblem:
    class State(_StateBase):
        def __init__(self, s=None, v=None, w=None):
            _StateBase.__init__(self, s, v)
            self.score = 0 if s == None else s.score + w(s.v, v)
            
    def __init__(self, G, w):
        self.G, self.w = G, w
        
    def initial_states(self):
        yield TspAsBranchAndBoundProblem.State(v=next(iter(self.G.V)))

    def is_final(self, s):
        return s.len == len(self.G.V)-1 and (s.v, s.head()) in self.G.E

    def decisions(self, s):
        if s.len < len(self.G.V):
            visited = s.visited()
            for v in self.G.succs(s.v):
                if v not in visited:
                    yield v

    def take_decision(self, s, v):
        return TspAsBranchAndBoundProblem.State(s, v, self.w)

    def destination_is_promising(self, s, v):
        return True

    def solution(self, s):
        return s.score + self.w(s.v, s.head())

    def opt(self, a, b):
       return min(a, b)

    def optimistic(self, s):
        return s.score

    def suboptimal_solution(self):
        return None

    def pessimistic(self, s):
        return self.zero
    
    zero = infinity
    one = -infinity
#> bb

#< bb2
class TspAsBranchAndBoundProblem2(TspAsBranchAndBoundProblem):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None, minweights=None):
            _StateBase.__init__(self, s, sample(G.V, 1)[0] if v == None else v)
            if s == None: self.score = sum(minweights)
            else: self.score = s.score - minweights[s.len] + w(s.v, v) 
        
    def __init__(self, G, w):
        TspAsBranchAndBoundProblem.__init__(self, G, w)
        self.minweights = list(reversed(sorted(w.values())[:len(G.V)]))
        
    def initial_states(self):
        yield TspAsBranchAndBoundProblem2.State(G=self.G, minweights=self.minweights)

    def take_decision(self, s, v):
        return TspAsBranchAndBoundProblem2.State(s, v, self.G, self.w, self.minweights)
#> bb2

#< bb3
class TspAsBranchAndBoundProblem3(TspAsBranchAndBoundProblem2):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None, minweights=None):
            _StateBase.__init__(self, s, sample(G.V, 1)[0] if v == None else v)
            if s == None: self.known = 0 
            else: self.known = s.known + w(s.v, v)
            edges = self.edges()
            D, i = 0.0, 0
            for (u,v) in minweights:
                if (u,v) not in edges: 
                    D += minweights[u,v]
                    i += 1
                if i == len(minweights) - self.len: break
            self.score = self.known + D
            
        def edges(self):
            if self.parent == None: return set([])
            edges = self.parent.edges()
            edges.add((self.parent.v, self.v) )
            return edges
            
    def __init__(self, G, w):
        TspAsBranchAndBoundProblem2.__init__(self, G, w)
        aux = sorted((w[k], k) for k in w)[:len(G.V)]
        self.minweights = dict((k, v) for (v, k) in aux)

    def initial_states(self):
        yield TspAsBranchAndBoundProblem3.State(G=self.G, minweights=self.minweights)

    def take_decision(self, s, d):
        return TspAsBranchAndBoundProblem3.State(s, d, self.G, self.w, self.minweights)
#> bb3

#< bb4
class TspAsBranchAndBoundProblem4(TspAsBranchAndBoundProblem2):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None, best_departure=None):
            _StateBase.__init__(self, s, sample(G.V, 1)[0] if v == None else v)
            if s == None: self.score = sum(best_departure.values()) 
            else: self.score = s.score - best_departure[s.v] + w(s.v, v)
        
    def __init__(self, G, w):
        TspAsBranchAndBoundProblem2.__init__(self, G, w)
        self.best_departure = dict((u, min((w(u,v) for v in G.succs(u)), ifempty=infinity))\
                                    for u in G.V)

    def initial_states(self):
        yield TspAsBranchAndBoundProblem4.State(G=self.G, best_departure=self.best_departure)
        
    def take_decision(self, s, d):
        return TspAsBranchAndBoundProblem4.State(s, d, self.G, self.w, self.best_departure)

    def solution(self, s):
        return s.score - self.best_departure[s.v] + self.w(s.v, s.head())
#> bb4

#< bb5
class TspAsBranchAndBoundProblem5(TspAsBranchAndBoundProblem2):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None):
            _StateBase.__init__(self, s, sample(G.V, 1)[0] if v == None else v) 
            if s == None: self.known = 0
            else: self.known = s.known + w(s.v, v)
            unvisited = set(G.V) - self.visited()
            departures = unvisited.union([v]) if v != None else unvisited
            arrivals = unvisited.union([self.head()])
            unknown = sum(min((w(u,v_prime) for v_prime in G.succs(u) if v_prime in arrivals), ifempty=infinity)\
                           for u in departures)
            self.score = self.known + unknown
            
    def __init__(self, G, w):
        TspAsBranchAndBoundProblem2.__init__(self, G, w)

    def initial_states(self):
        yield TspAsBranchAndBoundProblem5.State(G=self.G, w=self.w)

    def take_decision(self, s, d):
        return TspAsBranchAndBoundProblem5.State(s, d, self.G, self.w)
    
    def solution(self, s):
        return s.known + self.w(s.v, s.head())
#> bb5

#< bb6
class TspAsBranchAndBoundProblem6(TspAsBranchAndBoundProblem2):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None, D=None):
            _StateBase.__init__(self, s, sample(G.V, 1)[0] if v == None else v)
            if s == None: self.score = D[v]
            else: self.score = s.score + w(s.v, v) - D[s.v] + D[v]
            
    def __init__(self, G, w, graphFactory=lambda E: Digraph(E=E)):
        TspAsBranchAndBoundProblem2.__init__(self, G, w)
        if G.directed:
            Ginv = graphFactory(E=[(u,v) for (v,u) in w])
            winv = WeightingFunction(((u,v), w(u,v)) for (v,u) in w)
        else:
            Ginv = G
            winv = w
        self.first_vertex = sample(G.V, 1)[0]
        self.D = dict(Dijkstra_shortest_distance_one_to_all(Ginv, winv, self.first_vertex))

    def initial_states(self):
        yield TspAsBranchAndBoundProblem6.State(\
            v=self.first_vertex, G=self.G, w=self.w, D=self.D)

    def take_decision(self, s, v):
        return TspAsBranchAndBoundProblem6.State(s, v, self.G, self.w, D=self.D)
#> bb6


#< bb7
def distance_avoiding_vertices(G, d, forbidden, s, t):
    D = dict((v, infinity) for v in G.V)
    D[s] = 0
    frontier = MinHeapMap(D.items())
    added = set(forbidden)
    while len(frontier) > 0:
        v = frontier.extract_opt()
        added.add(v)
        if v == t: break
        for w in G.succs(v):
            if w not in added and D[v] + d(v,w) < D[w]:
                frontier[w] = D[w] = D[v] + d(v,w)
    return D.get(t, infinity)

class TspAsBranchAndBoundProblem7(TspAsBranchAndBoundProblem2):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None):
            _StateBase.__init__(self, s, v)
            if s == None: self.known = 0
            else: self.known = s.known + w(s.v, v)
            h = self.head()
            forbidden = self.visited() - set([h, v])
            self.score = self.known + distance_avoiding_vertices(G, w, forbidden, v, h)
            
    def __init__(self, G, w):
        TspAsBranchAndBoundProblem2.__init__(self, G, w)
        self.first_vertex = sample(G.V, 1)[0]

    def initial_states(self):
        yield TspAsBranchAndBoundProblem7.State(v=self.first_vertex, G=self.G, w=self.w)

    def take_decision(self, s, v):
        return TspAsBranchAndBoundProblem7.State(s, v, self.G, self.w)
    
    def solution(self, s):
        return s.known + self.w(s.v, s.head())
#> bb7

#< bb8
def MST_weight_avoiding_vertices(G, d, added, u):
    weight = 0
    frontier = MinHeapMap(((v, d(u,v)) for v in G.succs(u) if v not in added))
    added.add(u)
    while len(frontier) > 0:
        (v, duv) = frontier.extract_opt_item()
        added.add(v)
        weight += duv
        for w in G.succs(v):
            if w not in added and (w not in frontier or d(v, w) < frontier[w]):
                frontier[w] = d(v,w)
    return weight

class TspAsBranchAndBoundProblem8(TspAsBranchAndBoundProblem2):
    class State(_StateBase):
        def __init__(self, s=None, v=None, G=None, w=None):
            _StateBase.__init__(self, s, v)
            if s == None: self.known = 0
            else: self.known = s.known + w(s.v, v)
            forbidden = self.visited() - set([v])
            self.score = self.known + MST_weight_avoiding_vertices(G, w, forbidden, v)
        
    def __init__(self, G, w):
        TspAsBranchAndBoundProblem2.__init__(self, G, w)
        self.first_vertex = sample(G.V, 1)[0]

    def initial_states(self):
        yield TspAsBranchAndBoundProblem8.State(v=self.first_vertex, G=self.G, w=self.w)

    def take_decision(self, s, v):
        return TspAsBranchAndBoundProblem8.State(s, v, self.G, self.w)
#> bb8