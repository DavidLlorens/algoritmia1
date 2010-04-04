from algoritmia.datastructures.digraphs.digraph import UndirectedGraph
from algoritmia.problems.spanningtrees.kruskal import KruskalsMinimumSpanningForestFinder
from algoritmia.problems.traversals.depthfirst import DepthFirstTraverser
from algoritmia.problems.travelingsalesperson.nearestneighbor import d

class SpanningTreeTravelingSalesPerson:#[full
    def travel(self, points: "IList<(Real, Real)>") -> "Iterable<(Real, Real)>":
        G = UndirectedGraph(E=[(a, b) for a in points for b in points if a!=b])
        tree = KruskalsMinimumSpanningForestFinder().minimum_spanning_forest(G, d)
        MST = UndirectedGraph(V=points, E=tree)
        dft = DepthFirstTraverser()
        path = list(dft.traverse(MST, points[0], preorder_visitor=lambda u, v: v))
        path.append(points[0])
        return path#]full