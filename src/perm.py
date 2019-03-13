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

for max_edge_count, solution in result[0].items():
    print("Best solution for " + str(max_edge_count) + " edges: " + str(solution))
    print("Deviance: " + str(result[1][max_edge_count]))
    print(result[2][max_edge_count])
    print()
