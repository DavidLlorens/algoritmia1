#coding: latin1
import unittest
from algoritmia.problems.shortestpaths.acyclic import DagShortestPathsFinder, MemoizedDagShortestPathsFinder
from algoritmia.problems.shortestpaths.positive import DijkstraWithPriorityDictShortestPathsFinder
from algoritmia.datastructures.digraphs import Digraph, WeightingFunction
from algoritmia.data.iberia import iberia, cities, km, coords

class TestShortest(unittest.TestCase):
    def setUp(self):
        self.iberia = Digraph(V=cities)
        ikm = {}
        for i in cities:
            for j in iberia.succs(i):
                c1 = coords[i]
                c2 = coords[j]
                if c1[0] < c2[0]:
                    self.iberia.E.add((i, j))
                    ikm[i, j] = km(i, j)
        self.km = WeightingFunction(ikm, symmetrical=False)
        self.unconnected = Digraph(E={0: [1,2], 1:[2,3], 2:[5, 6], 3: [5], 4: [2], 5: [6]})
        self.unconnected_weight = WeightingFunction((((u,v), 1) for (u,v) in self.unconnected.E))

        self.iterative = DagShortestPathsFinder()
        self.memoized = MemoizedDagShortestPathsFinder()
        self.dijkstra = DijkstraWithPriorityDictShortestPathsFinder()

    def test_DagShortestPathsFinder_distance(self):
        d = self.dijkstra.distance(self.iberia, self.km, 'Madrid', 'Gandia')
        self.assertEquals(d, self.iterative.distance(self.iberia, self.km, 'Madrid', 'Gandia'))

    def test_MemoizedDagShortestPathsFinder_distance(self):
        d = self.dijkstra.distance(self.iberia, self.km, 'Madrid', 'Gandia')
        self.assertEquals(d, self.memoized.distance(self.iberia, self.km, 'Madrid', 'Gandia'))

    def test_DagShortestPathsFinder_shortest_path(self):
        d = self.dijkstra.shortest_path(self.iberia, self.km, 'Madrid', 'Gandia')
        self.assertEquals(d, self.iterative.shortest_path(self.iberia, self.km, 'Madrid', 'Gandia'))

    def test_MemoizedDagShortestPathsFinder_some_to_some_distance(self):
        d = self.dijkstra.some_to_some_distance(self.iberia, self.km,  ['Madrid', 'Sevilla'], ['Gandia', 'Barcelona'])
        self.assertEquals(d, self.memoized.some_to_some_distance(self.iberia, self.km, ['Madrid', 'Sevilla'], ['Gandia', 'Barcelona']))

    def test_DagShortestPathsFinder_some_to_some_shortest_path(self):
        b1 = dict(self.dijkstra.some_to_some_backpointers(self.iberia, self.km, ['Madrid', 'Sevilla'], ['Gandia', 'Barcelona']))
        b2 = dict(self.iterative.some_to_some_backpointers(self.iberia, self.km, ['Madrid', 'Sevilla'], ['Gandia', 'Barcelona']))
        self.assertTrue(all(b1[k] == b2[k] for k in cities if k in b1 and k in b2) and len(b1) > 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()