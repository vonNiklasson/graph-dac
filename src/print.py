from GraphConverter import GraphConverter as gc
from GraphPrinter import GraphPrinter
from graphs import hossein

network = gc.from_dict(hossein)
GraphPrinter.draw(network)
