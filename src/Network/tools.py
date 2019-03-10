"""
Get the average value of the given nodes.
Can select which nodes should be used by giving node ids as the second argument.
"""
def nodes_average(nodes, ids=[]):
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


"""
Update the nodes value to the average of its neighbours
"""
def update_node_average(nodes, edges, id):
    # Make a new list of all the neighbouring ID's and its own ID
    neighbour_ids = [id] + edges[id]
    # Get the average value of the neighbours and itself
    neighbour_average = nodes_average(nodes, neighbour_ids)
    # Update the inner value of the node
    nodes[id].update_value(neighbour_average)

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
