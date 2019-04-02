from GraphConverter import GraphConverter as gc
from GraphSolver import GraphSolver
from GraphPrinter import GraphPrinter

from graphs import hossein

g = gc.from_dict(hossein)

gs = GraphSolver()

y = gs.solve(g, 6)

print y['graphs']



GraphPrinter.draw(y['graphs'])

