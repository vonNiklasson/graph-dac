from GraphConverter import GraphConverter as gc
from GraphSolver import GraphSolver
from GraphPrinter import GraphPrinter

from graphs import hossein as figure

g = gc.from_dict(figure)


a = GraphSolver.get_neighbour_matrix(g)
w = GraphSolver.get_eigenvalues(a)

print w.tolist()

print GraphSolver.second_largest(w)
