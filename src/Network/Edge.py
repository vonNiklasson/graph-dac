from .Node import Node


class Edge:

    _cost = 0
    _origin = None
    _destination = None

    def __init__(self, cost, origin, destination):
        self._cost = cost
        self._origin = origin
        self._destination = destination

    @classmethod
    def from_nodes(cls, origin, destination):
        """

        :param origin:
        :type origin: Node
        :param destination:
        :type destination: Node
        """
        cost = origin.distance()
        edge = Edge(cost, origin, destination)
        return edge

    def get_cost(self):
        return self._cost
