
def nodes_average(nodes, ids=[]):
    """
    Get the average value of the given nodes.
    Can select which nodes should be used by giving node ids as the second argument.

    :param nodes:   The complete node structure to get the average of.
    :param ids:     (optional) The ID's of the nodes to get the average of.
    :return:        The average value of the given nodes.
    """
    keys = list(nodes.keys()) if ids == [] else ids
    return sum([float(node.get_outer()) if key in keys else 0 for key, node in nodes.items()]) / len(keys)


def nodes_deviance(nodes):
    """
    Get the value of the deviance across the nodes.

    :param nodes:   Set of nodes to calculate from.
    :return:        The deviance of the nodes
                    (maximum outer node value - minimum outer node value)
    """
    # Get first key of nodes
    first_key = next(iter(nodes.keys()))
    # Set the min and max to a temp value
    node_min = nodes[first_key].get_outer()
    node_max = nodes[first_key].get_outer()

    # Iterate over the nodes and get the maximum deviance of the network.
    for _, node in nodes.items():
        node_min = min(node_min, node.get_outer())
        node_max = max(node_max, node.get_outer())

    # Calculate the deviance
    deviance = node_max - node_min

    return deviance


def nodes_deviance_p(nodes):
    """
    Get the percentage value of the deviance across the nodes

    :param nodes:   Set of nodes to calculate from.
    :return:        The percentage deviance of the nodes
                    (maximum outer node value - minimum outer node value) / average
    """
    average = nodes_average(nodes)
    deviance = nodes_deviance(nodes)
    return deviance / average


def update_node_average(nodes, edges, id):
    """
    Update the nodes value to the average of its neighbours.

    :param nodes:   The nodes to check on.
    :param edges:   The edge structure of the nodes.
    :param id:      The ID of the origin node to get the neighbours of.
    """
    if id in edges:
        # Make a new list of all the neighbouring ID's and its own ID
        neighbour_ids = [id] + edges[id]
    else:
        neighbour_ids = [id]
    # Get the average value of the neighbours and itself
    neighbour_average = nodes_average(nodes, neighbour_ids)
    # Update the inner value of the node
    nodes[id].update_value(neighbour_average)


def has_edge(edges, origin, dest):
    """
    Checks if there's an edge between 2 nodes.

    :param edges:   The set of edges to check from.
    :param origin:  The origin node.
    :param dest:    The destination node.
    :return:        True if there's an edge between origin and dest, otherwise False.
    """
    if origin in edges:
        if dest in edges[origin]:
            return True
    if dest in edges:
        if origin in edges[dest]:
            return True
    return False


def count_edges(edges):
    """
    Counts the number of edges in the graph and excludes bidirectional edges.

    :param edges:   The edges in the graph to count
    :type edges:    dict[int, list[int]]
    :return:        The number of edges in the graph (single-directional).
    :rtype:         int
    """

    # Normalised edges (non-bidirectional)
    single_edges = {}  # type: dict[int, list[int]]
    # Create an edge counter
    edge_count = 0  # type: int

    # Iterate over each node in the edge list
    for node_id, neighbours in edges.items():
        # Iterate over each neighbour
        for neighbour in neighbours:
            # Sort out the maximum and minimum node id
            min_node = min(node_id, neighbour)
            max_node = max(node_id, neighbour)
            # Check if there's an edge between the 2 nodes
            if not has_edge(single_edges, min_node, max_node):
                if min_node not in single_edges:
                    single_edges[min_node] = []
                # If not, store only the minimum number of edges needed (remove bi-directional)
                single_edges[min_node].append(max_node)
                # Add one edge to the counter
                edge_count = edge_count + 1

    return edge_count


def print_nodes_values(nodes):
    for key, node in nodes.items():
        print(str(key) + ": " + str(node.get_inner()))


def print_nodes_headers(nodes):
    row = str("ITER").rjust(5) + " |"
    row += str("AVG").rjust(8) + " |"
    row += str("DEV").rjust(8) + " |"
    for key, _ in nodes.items():
        row += ("#" + str(key)).rjust(8) + " |"
    print(row)


def print_node_values_row(iteration, nodes):
    row = str(iteration).rjust(5) + " |"
    row += str(round(nodes_average(nodes), 2)).rjust(8) + " |"
    row += str(round(nodes_deviance(nodes), 2)).rjust(8) + " |"
    for key, node in nodes.items():
        row += str(round(node.get_inner(), 2)).rjust(8) + " |"
    print(row)
