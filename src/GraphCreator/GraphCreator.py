import copy

from Network import Network


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

    def solve(self):
        # Store the minimum and maximum edges required to find a solution
        min_edges = len(self._nodes) - 1
        if self._max_edges == -1:
            max_edges = len(self._nodes) - 1
        else:
            max_edges = self._max_edges

        # Create a network object
        network = Network()
        network.add_nodes(self._nodes)

        # Store a graph list with possible solutions
        graph_list = {}
        optimal_graph_list = {}
        for edge_count in range(min_edges, max_edges+1):
            graph_list[edge_count] = None
            # Set a large number to compare to later
            optimal_graph_list[edge_count] = float('inf')

        # Get the smallest and largest number of nodes
        max_node = next(iter(self._nodes.keys()))
        min_node = next(iter(self._nodes.keys()))

        # Iterate over all nodes to find the largest and smallest node id
        for temp_node_id, _ in self._nodes.items():
            max_node = max(max_node, temp_node_id)
            min_node = min(min_node, temp_node_id)

        def dfs(node_id, neighbour_id, edge_count):
            # If we're trying to create an edge from an unexisting node, don't bother
            if node_id not in self._nodes:
                return

            # If we've exceeded the maximum number of edges allowed, don't bother
            if edge_count > max_edges:
                return

            # Make sure that the node id exists in the edge dict
            if node_id not in self._edges:
                self._edges[node_id] = []

            # We don't want to iterate over the last node
            if node_id < max_node:
                # Try finding a solution without adding any edges
                dfs(node_id + 1, node_id + 2, edge_count)

                if neighbour_id in self._nodes:

                    # Iterate over all increasing neighbours
                    for next_node, _ in self._nodes.items():
                        # Make sure that the next node id is greater than the current node
                        if next_node >= neighbour_id:
                            # Add edge between node_id and next_node
                            self._edges[node_id].append(next_node)
                            # Iterate over next adding neighbour
                            dfs(node_id, next_node + 1, edge_count + 1)
                            # Remove that neighbour and try with another one
                            self._edges[node_id].remove(next_node)
            elif edge_count >= min_edges:
                network.add_edges(self._edges)
                if network.is_graph_connected():
                    result = network.solve()
                    if result[1] < optimal_graph_list[edge_count]:
                        optimal_graph_list[edge_count] = result[1]
                        graph_list[edge_count] = copy.deepcopy(self._edges)
                network.reset_edges()

        dfs(min_node, min_node + 1, 0)

        return optimal_graph_list, graph_list
