import math


class Node:

    _node_id = None

    _inner = 0.0
    _outer = 0.0

    _coordinates = (0, 0)

    def __init__(self, node_id, initial, coordinates=(0, 0)):
        self._node_id = node_id
        self._inner = float(initial)
        self._coordinates = coordinates
        self.extract()

    def get_node_id(self):
        return self._node_id

    def extract(self):
        self._outer = self._inner

    def update_value(self, new_value):
        self._inner = new_value

    def get_inner(self):
        return self._inner

    def get_outer(self):
        return self._outer

    def get_coordinates(self):
        return self._coordinates

    def distance(self, node):
        return pow(self._coordinates[0] - node.get_coordinates()[0], 2) + \
               pow(self._coordinates[1] - node.get_coordinates()[1], 2)
