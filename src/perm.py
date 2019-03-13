

nodes = {
    1: 1,
    2: 2,
    3: 3
}
max_edges = 5

edges = {}

counter = 0


def dfs(node_id, neighbour_id, edge_count):

    global counter
    # Edge cond
    print(edges)
    counter = counter + 1

    if node_id not in nodes or neighbour_id not in nodes:
        return

    if edge_count > max_edges:
        return

    # Make sure that the node id exists in the edge dict
    if node_id not in edges:
        edges[node_id] = []

    #print("node_id: " + str(node_id) + ", neighbour_id: " + str(neighbour_id))

    # Try finding a solution without adding any edges
    dfs(node_id+1, node_id+1, edge_count)

    # Iterate over all increasing neighbours
    for next_node, _ in nodes.items():
        # Make sure that the next node id is greater than the current node
        if next_node <= node_id or next_node < neighbour_id:
            continue
        print("+ "+str(node_id)+"-"+str(next_node))
        # Add edge between node_id and next_node
        edges[node_id].append(next_node)
        # Iterate over next adding neighbour
        dfs(node_id, next_node+1, edge_count+1)
        print("- "+str(node_id)+"-"+str(next_node))
        # Remove that neighbour and try with another one
        edges[node_id].remove(next_node)



dfs(1, 1, 0)


print(counter)

def has_edge(edges, origin, dest):
    if origin in edges:
        if dest in edges[origin]:
            return True
    if dest in edges:
        if origin in edges[dest]:
            return True
    return False
