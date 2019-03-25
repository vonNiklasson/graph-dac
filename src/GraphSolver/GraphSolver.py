import networkx as nx
from .GraphConverter import GraphConverter as gc

class GraphSolver: 

    _original = None   
    _min_edges = 0
    _max_edges = 0

    @staticmethod
    def solve(g, m_edges):
        """
        Generates a complicated dictionary with the final edge list which yields the minimum number of iterations
        to find the distributed average consensus.

        :return:    A dictionary of solutions.
        :rtype:     dict
        """
        # Store the minimum and maximum edges required to find a solution
        self._min_edges = len(g.nodes()) - 1
        if  m_edges < self.min_edges:
            self._max_edges = self._min_edges
        
        self._original = g
        # Copy the graph given to a new graph
        copied_graph = copy.deepcopy(g)

        # Create a new network object
        #network = Network()
        #network.add_nodes(self._nodes)
        #network.set_max_iterations(100)
        #network.set_deviance(0.1)

        # Count the number of bidirectional edges.
        current_edge_count = g.size.

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
            if not g.has_node(node_id):
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

                if g.has_node(neighbour_id):
                    # Iterate over all increasing neighbours
                    nodes = g.nodes(data=true)
                    nodes = nodes[node_id:]
                    for next_node, in nodes:
                        # Make sure that it doesn't already exists an edge there.
                        # If there would already be an edge, it's supposed to be there and won't be deleted.
                        if g.has_edge(node_id, next_node):
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
                # Make sure the graph is connected
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
