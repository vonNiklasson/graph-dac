from GraphConverter import GraphConverter as gc
from GraphSolver import GraphSolver
from GraphPrinter import GraphPrinter

from graphs import hossein

g = gc.from_dict(hossein)

gs = GraphSolver()

y = gs.solve(g, 8)

for edge_count, graph in y['graphs'].items():
    if graph is not None:
        print "Graph with " + str(edge_count) + " edges: " + str(y['convergence_rate'][edge_count])
        GraphPrinter.draw(graph)
        raw_input("Press enter to draw next graph")

print "No more graphs"