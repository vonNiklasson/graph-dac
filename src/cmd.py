import graphs
import sys
from Network import Network

if len(sys.argv) > 1:
    figure = getattr(graphs, sys.argv[1])
else:
    figure = graphs.cross

if len(sys.argv) > 2:
    deviance_threshold = float(sys.argv[2])
else:
    deviance_threshold = 0.01


nodes = figure["V"]
edges = figure["E"]

network = Network()

network.set_max_iterations(1000)

network.set_deviance(deviance_threshold)

network.add_edges(edges)
network.add_nodes(nodes)

result = network.solve()

print("")
print("Solved:     " + str(result[0]))
print("Iterations: " + str(result[1]))
print("Deviance:   " + str(result[2]))
