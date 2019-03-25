import networkx as nx


class GraphConverter:

    def __init__(self, netx):
        pass

    @classmethod
    def from_dict(cls, g):
        netx = nx.Graph()
        nodes = g["V"]
        edges = g["E"]

        for node_id, node in nodes.items():
            netx.add_node(node_id, value=node[0], coordinates=node[1])

        for origin, destinations in edges.items():
            for destination in destinations:
                print origin, destination

        for node_id, node_attrs in netx.nodes().items():
            print str(node_id) + ": " + str(node_attrs)
        return netx

    def init_cord_rand(netx):

        for node_id, node_attrs in netx.nodes().items():
            node_attrs = (random.randint(0,100), random.randint(0, 100))
        
        for node_id, node_attrs in netx.nodes().items():
            print str(node_id) + ": " + str(node_attrs)
