#coding: latin1

import unittest
from algoritmia.datastructures.digraphs import (UndirectedGraph, Digraph, AdjacencyDigraph, 
                                              LinkedListSetAdjacencyDigraph, 
                                              ListSetAdjacencyDigraph, SetAdjacencyDigraph, 
                                              AdjacencyMatrixDigraph, InvAdjacencyDigraph,
                                              WeightingFunction)
from algoritmia.datastructures.sets import IntSet
from algoritmia.datastructures.maps import IntKeyMap

class TestDigraphs(unittest.TestCase):
    def setUp(self):
        self.edges = [(0,1), (1,2), (2,3), (3,4), (4,5), (5,0), (0,3), (3,0), (0,2), (0,4), (0,7)]
        self.g1 = Digraph(V=range(8), E=self.edges)
        self.g1bis = Digraph(E=self.edges)
        self.g1bis.V.add(6)
        self.g2 = AdjacencyDigraph(V=range(8), E=self.edges, directed=True, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1), 
                                 createSet=lambda V: IntSet(capacity=max(V)+1))
        self.g3 = LinkedListSetAdjacencyDigraph(V=range(8), E=self.edges, directed=True, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1))
        self.g4 = ListSetAdjacencyDigraph(V=range(8), E=self.edges, directed=True, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1))
        self.g5 = SetAdjacencyDigraph(V=range(8), E=self.edges, directed=True, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1))
        self.g6 = AdjacencyMatrixDigraph(V=range(8), E=self.edges, directed=True)
        self.g7 = InvAdjacencyDigraph(V=range(8), E=self.edges, directed=True, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1), 
                                 createSet=lambda V: IntSet(capacity=max(V)+1))
        edges = self.edges + [(1,1)]
        self.g8 = InvAdjacencyDigraph(V=range(8), E=edges, directed=True, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1), 
                                 createSet=lambda V: IntSet(capacity=max(V)+1))
    
    def test_readonly(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            self.assertEqual(len(g.V), 8)
            self.assertEqual(len(g.E), len(self.edges))
            for (u,v) in self.edges:
                self.assertTrue((u,v) in g.E)
            for u in g.V:
                succ = set(v for (uu, v) in self.edges if uu == u)
                pred = set(v for (v, uu) in self.edges if uu == u)
                self.assertEqual(succ, set(g.succs(u)))
                self.assertEqual(pred, set(g.preds(u)))
            self.assertFalse((0,0) in g.E)
            
            self.assertEqual(g.out_degree(0), 5)
            self.assertEqual(g.in_degree(0), 2)
            
    def test_remove_self_loop(self):
        self.g8.V.remove(1)
        self.assertEqual(9, len(self.g8.E))
    
    def test_edit_edges(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            g.E.add((7,1))
            self.assertEqual(len(g.E), len(self.edges)+1)
            self.assertTrue((7,1) in g.E)
            self.assertFalse((1,7) in g.E)
            g.E.remove((0,7))
            self.assertFalse((0,7) in g.E)
            self.assertEqual(len(g.E), len(self.edges))
            
class TestGraphs(unittest.TestCase):
    def setUp(self):
        self.edges = [(0,1), (1,2), (2,3), (3,4), (4,5),(5,0), (0,3), (3,0), (0,2), (0,4), (0,7)]
        self.undirected_edges = set()
        for (u,v) in self.edges: 
            self.undirected_edges.add((u,v))
            self.undirected_edges.add((v,u))
        self.g1 = UndirectedGraph(V=range(8), E=self.edges)
        self.g1bis = UndirectedGraph(E=self.edges)
        self.g1bis.V.add(6)
        self.g2 = AdjacencyDigraph(V=range(8), E=self.edges, directed=False, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1), 
                                 createSet=lambda V: IntSet(capacity=max(V)+1))
        self.g3 = LinkedListSetAdjacencyDigraph(V=range(8), E=self.edges, directed=False, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1))
        self.g4 = ListSetAdjacencyDigraph(V=range(8), E=self.edges, directed=False, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1))
        self.g5 = SetAdjacencyDigraph(V=range(8), E=self.edges, directed=False, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1))
        self.g6 = AdjacencyMatrixDigraph(V=range(8), E=self.edges, directed=False)
        self.g7 = InvAdjacencyDigraph(V=range(8), E=self.edges, directed=False, 
                                 createMap=lambda V: IntKeyMap(capacity=max(V)+1), 
                                 createSet=lambda V: IntSet(capacity=max(V)+1))
    def test_V_contains(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            for i in range(8):
                self.assertTrue(i in g.V)
                self.assertFalse(8+i in g.V)

    def test_E_contains(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            for (u,v) in self.edges:
                self.assertTrue((u,v) in g.E)
                self.assertFalse((u,v+8) in g.E)
                self.assertFalse((u+8,v) in g.E)

    def test_remove_vertex(self):
        self.g7.V.remove(1)
        self.assertEqual(16, len(self.g7.E))

    def test_V_len(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            self.assertEqual(len(g.V), 8)

    def test_E_len(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            self.assertEqual(len(g.E), len(self.undirected_edges))

    def test_V_repr(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            self.assertEqual(set(g.V), set(eval(repr(g.V))))
        
    def test_E_repr(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            self.assertEqual(set(g.E), set(eval(repr(g.E))))

    def test_succs_and_preds(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            for u in g.V:
                succ = set(v for (uu, v) in self.undirected_edges if uu == u)
                pred = set(v for (v, uu) in self.undirected_edges if uu == u)
                self.assertEqual(succ, set(g.succs(u)))
                self.assertEqual(pred, set(g.preds(u)))

    def test_out_degree(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:                
            self.assertEqual(g.out_degree(0), 6)
            for v in g.V:
                self.assertEqual(g.out_degree(v), g.in_degree(v))
    
    def test_repr(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            gg = eval(repr(g))
            self.assertEqual(set(g.V), set(gg.V))
            self.assertEqual(set(g.E), set(gg.E))
    
    def test_edit_edges(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            g.E.add((7,1))
            self.assertEqual(len(g.E), len(self.undirected_edges)+2)
            self.assertTrue((7,1) in g.E)
            self.assertTrue((1,7) in g.E)
            
            g.E.remove((0,7))
            self.assertFalse((7,0) in g.E)
            self.assertFalse((0,7) in g.E)

            g.E.add_unchecked((1,3))
            self.assertTrue((1,3) in g.E)
            self.assertTrue((3,1) in g.E)

    def test_edit_vertices(self):
        for g in self.g1, self.g1bis, self.g2, self.g3 ,self.g4, self.g5, self.g6, self.g7:
            g.V.add(6)
            self.assertTrue(6 in g.V)
            self.assertFalse((0,6) in g.E)
            self.assertFalse((6,0) in g.E)
            
            if g == self.g6: # Por cobertura
                g.V.add(10)
            
            g.V.remove(0)
            self.assertFalse((1,0) in g.E)
            self.assertFalse((0,1) in g.E)

class TestRedimDigraphs(unittest.TestCase):
    def setUp(self):
        self.edges = [(0,1), (1,2), (2,3), (3,4), (4,5),(5,0), (0,3), (3,0), (0,2), (0,4), (0,7)]
        self.g = AdjacencyDigraph(V=range(8), E=self.edges, directed=True, 
                                createMap=lambda V: IntKeyMap(capacity=max(V)+1), 
                                createSet=lambda V: IntSet(capacity=max(V)+1),
                                redimMap=lambda map, maxkey: map.set_capacity(max(map.capacity, maxkey+1)),
                                redimSet=lambda set, maxkey: set.set_capacity(max(set.capacity, maxkey+1)))

    def test_edit_edges(self):
        for g in self.g,:
            g.E.add((7,1))
            self.assertEqual(len(g.E), len(self.edges)+1)
            self.assertTrue((7,1) in g.E)
            self.assertFalse((1,7) in g.E)
            
            g.E.remove((0,7))
            self.assertFalse((7,0) in g.E)
            self.assertFalse((0,7) in g.E)
            
            g.E.add((12, 1))
            self.assertTrue((12,1) in g.E)
            self.assertFalse((1,12) in g.E)
            
            g.E.add((1, 12))
            self.assertTrue((1,12) in g.E)
            
class TestWeightingFunction(unittest.TestCase):
    def setUp(self):
        self.sym = WeightingFunction([((0,0), 1), ((1,1), 2), ((1,2), 3)], symmetrical=True)
        self.asym = WeightingFunction([((0,0), 1), ((1,1), 2), ((1,2), 3)], symmetrical=False)
    
    def test_getitem(self):
        self.assertEqual(self.sym(0,0), 1)
        self.assertEqual(self.sym(1,1), 2)
        self.assertEqual(self.sym(1,2), 3)
        self.assertEqual(self.sym(2,1), 3)
        self.assertEqual(self.asym(0,0), 1)
        self.assertEqual(self.asym(1,1), 2)
        self.assertEqual(self.asym(1,2), 3)
        self.assertRaises(KeyError, self.asym.__call__, (2,1))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()