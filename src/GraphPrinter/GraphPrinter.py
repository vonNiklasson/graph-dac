import networkx as nx
import matplotlib.pyplot as plt


class GraphPrinter:

    @staticmethod
    def draw(nx_graph):
        """
        Takes a networkx graph and prints the nodes
        with given edges in the fixed positions.

        :param nx_graph: The networkx object to show the graph from.
        :type nx_graph: networkx.Graph
        """
        # Create a dict with fixed positions.
        fixed_positions = {}

        # Extracts the positions and stores them in the dict
        for node in nx_graph.nodes(data=True):  # type: tuple
            if 'coordinates' in node[1]:
                fixed_positions[node[0]] = node[1].get('coordinates')

        # Get the indexes of the fixed positions
        fixed_nodes = fixed_positions.keys()
        # Do some magic
        pos = nx.spring_layout(nx_graph, pos=fixed_positions, fixed=fixed_nodes)
        # Draw the graph
        nx.draw_networkx(nx_graph, pos)
        # Show the graph
        plt.show()
