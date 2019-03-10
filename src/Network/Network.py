from .Node import Node
from . import tools


class Network:

    _nodes = {}
    _edges = {}

    __deviance = 0.01
    __max_iterations = 1000

    def __init__(self):
        self._nodes = {}
        self._edges = {}
        self.__deviance = 0.01

    def set_deviance(self, deviance):
        """
        Sets the maximum number of deviance (in value) of the maximum spread of the lowest to highest node before
        it's deemed as complete.

        :param deviance:    The maximum deviance.
        """
        self.__deviance = deviance

    def set_max_iterations(self, max_iterations):
        """
        Sets the maximum number of iterations for the network before giving up on finding a solution.
        Defaults to 1 000.

        :param max_iterations:  The maximum number of iterations to run.
        """
        self.__max_iterations = max_iterations

    def add_node(self, node_id, node_value):
        """
        Adds a node with given id and value.

        :param node_id:     The ID of the node.
        :param node_value:  The initial value of the node.
        """
        self._nodes[node_id] = Node(node_value)

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

    def add_edge(self, origin, dest):
        """
        Adds a bidirectional edge between origin and dest.

        :param origin:  The source ID of the node.
        :param dest:    The destination ID of the node.
        """
        # Checks if the origin node is in the set of edges.
        if origin not in self._edges:
            # If not, adds it.
            self._edges[origin] = []

        # Checks if the destination node is in the set of neighbours for origin node.
        if dest not in self._edges[origin]:
            # If not, adds it.
            self._edges[origin].append(dest)

        # Checks if the destination node is in the set of edges.
        if dest not in self._edges:
            # If not, adds it.
            self._edges[dest] = []

        # Checks if the origin node is in the set of neighbours for destination node.
        if origin not in self._edges[dest]:
            # If not, adds it.
            self._edges[dest].append(origin)

    def add_edges(self, edges):
        for start_node, end_nodes in edges.items():
            for end_node in end_nodes:
                self.add_edge(start_node, end_node)

    def solve(self, silent=False):
        if not silent:
            # Print the header and the initial state
            tools.print_nodes_headers(self._nodes)
            tools.print_node_values_row(0, self._nodes)

        counter = 0
        deviance = tools.nodes_deviance(self._nodes)

        # Continue while the deviance is larger than a certain value
        while deviance > self.__deviance:
            # Update the iteration counter
            counter += 1

            # Iterate through each item and update its value
            for id in self._nodes:
                tools.update_node_average(self._nodes, self._edges, id)
            # Move the inner value to the outer value
            for _, node in self._nodes.items():
                node.extract()

            if not silent:
                # Print each nodes current outer value
                tools.print_node_values_row(counter, self._nodes)

            # Calculate teh deviance
            deviance = tools.nodes_deviance(self._nodes)

            if counter > self.__max_iterations:
                return False, counter, deviance

        return True, counter, deviance
