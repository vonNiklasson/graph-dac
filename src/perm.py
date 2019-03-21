from GraphCreator import GraphCreator
from Graph import tools
import graphs

nodes = graphs.hossein["V"]
edges = graphs.hossein["E"]

max_edges = tools.count_edges(edges) + 2


print("----- Given -----")
print("")
print("Nodes:")
print(nodes)
print("")
print("Edges:")
print(edges)
print("")
print("")

gc = GraphCreator()
gc.add_nodes(nodes)
gc.add_edges(edges)
gc.set_max_edges(max_edges)

result = gc.solve()


print("----- Solutions -----")
print("")

for edge_count, _ in result["iterations"].items():
    print("Best solution for " + str(edge_count) + " edges: " + str(result["iterations"][edge_count]))
    print("Deviance: " + str(result["deviances"][edge_count]))
    print("Edges:")
    print(result["graphs"][edge_count])
    print("")
