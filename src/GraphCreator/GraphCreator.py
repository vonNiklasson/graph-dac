import copy
import networkx as nx


class GraphCreator:

    _nodes = {}
    _edges = {}
    _max_edges = 0

    def __init__(self):
        self._nodes = {}
        self._edges = {}
        self._max_edges = -1
        pass

    def set_max_edges(self, max_edges):
        self._max_edges = max_edges

    def add_node(self, node_id, node_value):
        """
        Adds a node with given id and value.

        :param node_id:     The ID of the node.
        :param node_value:  The initial value of the node.
        """
        self._nodes[node_id] = node_value

    def add_nodes(self, nodes):
        """
        Adds a range of nodes.

        :param nodes:   A dict of nodes given in key-value pairs.
                        Example: { id1: val1, id2, val2 ... }
        """
        # Iterates through the nodes
        for node_id, node_value in nodes.items():
            # Adds them one by one
            self.add_node(node_id, node_value)

    def add_edges(self, edges):
        self._edges = edges

    def solve(self):
        """
        Generates a complicated dictionary with the final edge list which yields the minimum number of iterations
        to find the distributed average consensus.

        :return:    A dictionary of solutions.
        :rtype:     dict
        """
        # Store the minimum and maximum edges required to find a solution
        min_edges = len(self._nodes) - 1
        if self._max_edges == -1:
            max_edges = len(self._nodes) - 1
        else:
            max_edges = self._max_edges

        # Copy the given edges to a new list
        edges = copy.deepcopy(self._edges)

        # Create a new network object
        network = Network()
        network.add_nodes(self._nodes)
        network.set_max_iterations(100)
        network.set_deviance(0.1)

        # Count the number of bidirectional edges.
        current_edge_count = tools.count_edges(edges)

        # Store a graph list with possible solutions
        graph_list = {}
        optimal_graph_list = {}
        deviance_graph_list = {}
        for possible_edge_count in range(min_edges, max_edges+1):
            graph_list[possible_edge_count] = None
            # Set a large number to compare to later
            optimal_graph_list[possible_edge_count] = float('inf')
            deviance_graph_list[possible_edge_count] = float('inf')

        # Get the smallest and largest id of the nodes
        min_node = next(iter(self._nodes.keys()))
        max_node = next(iter(self._nodes.keys()))

        # Iterate over all nodes to find the largest and smallest node id
        for temp_node_id, _ in self._nodes.items():
            min_node = min(min_node, temp_node_id)
            max_node = max(max_node, temp_node_id)

        def dfs(node_id, neighbour_id, edge_count):
            # If we're trying to create an edge from an unexisting node, don't bother
            if node_id not in self._nodes:
                return

            # If we've exceeded the maximum number of edges allowed, don't bother
            if edge_count > max_edges:
                return

            # Make sure that the node id exists in the edge dict
            if node_id not in edges:
                edges[node_id] = []

            # We don't want to iterate over the last node
            if node_id < max_node:
                # Try finding a solution without adding any edges
                dfs(node_id + 1, node_id + 2, edge_count)

                if neighbour_id in self._nodes:
                    # Iterate over all increasing neighbours
                    for next_node, _ in self._nodes.items():
                        # Make sure that the next node id is greater than the current node
                        if next_node >= neighbour_id:
                            # Make sure that it doesn't already exists and edge there.
                            # If there would already be an edge, it's supposed to be there and won't be deleted.
                            if tools.has_edge(edges, node_id, next_node):
                                continue

                            # Add edge between node_id and next_node
                            edges[node_id].append(next_node)
                            # Iterate over next adding neighbour
                            dfs(node_id, next_node + 1, edge_count + 1)
                            # Remove that neighbour and try with another one
                            edges[node_id].remove(next_node)

            elif edge_count >= min_edges:
                # Add the proposed edges in the network
                network.add_edges(edges)
                # Make sure the graph is corrected
                if network.is_graph_connected():
                    # Solve the problem
                    result = network.solve()
                    # If the new result yields a better result, store it instead
                    if result["iterations"] < optimal_graph_list[edge_count] or \
                        (result["iterations"] == optimal_graph_list[edge_count] and result["deviance"] < deviance_graph_list[edge_count]):
                        optimal_graph_list[edge_count] = result["iterations"]
                        deviance_graph_list[edge_count] = result["deviance"]
                        graph_list[edge_count] = copy.deepcopy(edges)
                network.reset_edges()

        dfs(min_node, min_node + 1, current_edge_count)

        return {
            "iterations": optimal_graph_list,
            "deviances": deviance_graph_list,
            "graphs": graph_list
        }
