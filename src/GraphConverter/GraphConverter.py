import networkx as nx
import random
import numpy
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
                GraphConverter.add_edge(netx, origin, destination)
                print origin, destination

        for node in netx.nodes(data=True):
            print node
        
        for edge in netx.edges(data = True):
            print edge

        return netx

    @classmethod
    def add_edge(cls, g, start, destination):
        # find start & end coordinates
        start_cord = g.node[start]['coordinates']
        destination_cord = g.node[destination]['coordinates']

        # subtract the coordinate values of the two points
        delta = tuple(numpy.subtract(destination_cord, start_cord))
        # the difference in position is squared  
        numpy.square(delta)
        # extract values from delta tuple
        deltax, deltay = delta
        # cost is the summation of the difference in x and y
        weight = deltax + deltay

        #add edge to graph
        g.add_edge(start, destination, weight = weight)


