import networkx as nx
from GraphConverter import GraphConverter as gc
import copy

class GraphSolver: 

    _copy = None
    _candidate = None   
    _min_edges = 0
    _max_edges = 0
    _deviance = 0.01
    _max_iterations = 1000

    def __init__(self):
        pass

    def solve(self, g, m_edges):
        """
        Generates a complicated dictionary with the final edge list which yields the minimum number of iterations
        to find the distributed average consensus.

        :return:    A dictionary of solutions.
        :rtype:     dict
        """
        # Store the minimum and maximum edges required to find a solution
        self._min_edges = len(g.nodes()) - 1
        if  m_edges < self._min_edges:
            self._max_edges = self._min_edges
        else:
            self._max_edges = m_edges
        
        # Copy the graph given to a new graph
        self._copy = copy.deepcopy(g)

        # Count the number of bidirectional edges.
        current_edge_count = g.size()

        # Store a graph list with possible solutions
        graph_list = {}
        optimal_graph_list = {}
        deviance_graph_list = {}
        for possible_edge_count in range(self._min_edges, self._max_edges+1):
            graph_list[possible_edge_count] = None
            # Set a large number to compare to later
            optimal_graph_list[possible_edge_count] = float('inf')
            deviance_graph_list[possible_edge_count] = float('inf')

        # Get the smallest and largest id of the nodes
        min_node = next(iter(g.nodes()))
        max_node = next(iter(g.nodes()))

        # Iterate over all nodes to find the largest and smallest node id
        for temp_node_id in iter(g.nodes()):
            min_node = min(min_node, temp_node_id)
            max_node = max(max_node, temp_node_id)

        def dfs(node_id, neighbour_id, edge_count):
            # If we're trying to create an edge from an unexisting node, don't bother
            if not self._copy.has_node(node_id):
                return

            # If we've exceeded the maximum number of edges allowed, don't bother
            if edge_count > self._max_edges:
                return

            # We don't want to iterate over the last node
            if node_id < max_node:
                # Try finding a solution without adding any edges
                dfs(node_id + 1, node_id + 2, edge_count)

                if self._copy.has_node(neighbour_id):
                    # Iterate over all increasing neighbours
                    nodes = list(iter(self._copy.nodes()))
                    nodes = nodes[node_id:]
                    for next_node in nodes:
                        if next_node >= neighbour_id:
                            # Make sure that it doesn't already exists an edge there.
                            # If there would already be an edge, it's supposed to be there and won't be deleted.
                            if g.has_edge(node_id, next_node):
                                continue

                            # Add edge between node_id and next_node
                            print str(node_id) + " " + str(next_node)
                            gc.add_edge(self._copy, node_id, next_node)
                            # Iterate over next adding neighbour
                            dfs(node_id, next_node + 1, edge_count + 1)
                            print "removing " + str(node_id) + " " + str(next_node)
                            print self._copy.has_edge(node_id, next_node)
                            # Remove that neighbour and try with another one
                            self._copy.remove_edge(node_id, next_node)

            elif edge_count >= self._min_edges:
                # Add the proposed edges in the network
                # Make sure the graph is connected
                if nx.is_connected(self._copy):
                    # Solve the problem
                    result = self.consensus_average(self._copy)
                    # If the new result yields a better result, store it instead
                    if result["iterations"] < optimal_graph_list[edge_count]:
                        optimal_graph_list[edge_count] = result["iterations"]
                        deviance_graph_list[edge_count] = result["deviance"]
                        self._candidate = copy.deepcopy(self._copy)
                self._copy = copy.deepcopy(g)

        dfs(min_node, min_node + 1, current_edge_count)

        return {
            "iterations": optimal_graph_list,
            "deviances": deviance_graph_list,
            "graphs": self._candidate
        }

    def consensus_average(self, g):
        graph = copy.deepcopy(g)

        counter = 0
        deviance = self.graph_deviance(graph)

        while self._deviance < deviance:
            # increment counter
            counter += 1
            # update values based on average value of neighboring
            self.update_values(graph)
            # update deviance
            deviance = self.graph_deviance(graph)
        
            if counter > self._max_iterations:
                return False, counter, deviance

        return{
            "Success": True,
            "iterations": counter,
            "deviance": deviance
        }


    def graph_deviance(self, g):
        node_min = float('Inf')
        node_max = float('-Inf')
        for node in g.nodes(data = True):
            node_min = min(node_min, node[1]['value'])
            node_max = max(node_max, node[1]['value'])

        return node_max - node_min

    def update_values(self, g):
        new_values = []
        nodes = g.nodes()

        for id in nodes:
            temp = g[id]['value']
            for neighbor in g.neighbor(id):
                temp += g[id]['value']
            new_values.append(temp)

        for node, new_value in map(None, nodes, new_values):
            g[node]['value'] = new_value


