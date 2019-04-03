from GraphConverter import GraphConverter as gc
from GraphSolver import GraphSolver
from GraphPrinter import GraphPrinter

from graphs import square

g = gc.from_dict(square)

gs = GraphSolver()

y = gs.solve(g, 6)

for edge_count, graph in y['graphs'].items():
    if graph is not None:
        print "Graph with " + str(edge_count) + " edges"
        GraphPrinter.draw(graph)
        raw_input("Press enter to draw next graph")

print "No more graphs"