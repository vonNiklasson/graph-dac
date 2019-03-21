import networkx as nx


class Graph:

    _nx = None

    def __init__(self):
        pass

    @classmethod
    def from_dict(cls, g):
        import networkx as nx
        nx = nx.Graph()
        nodes = g["V"]
        edges = g["E"]

        for node_id, node in nodes.items():
            nx.add_node(node_id, value=node[0], coordinates=node[1])

        for origin, destinations in edges.items():
            for destination in destinations:
                print origin, destination

        for node_id, node_attrs in nx.nodes().items():
            print str(node_id) + ": " + str(node_attrs)
