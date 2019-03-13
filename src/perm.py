from GraphCreator import GraphCreator

nodes = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6
}
max_edges = 8

edges = {}

gc = GraphCreator()
gc.add_nodes(nodes)
gc.set_max_edges(max_edges)

result = gc.solve()

print(result)

for edge_count, _ in result["iterations"].items():
    print("Best solution for " + str(edge_count) + " edges: " + str(result["iterations"][edge_count]))
    print("Deviance: " + str(result["deviances"][edge_count]))
    print(result["graphs"][edge_count])
    print()
