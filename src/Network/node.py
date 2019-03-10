
class Node:

    _inner = 0.0
    _outer = 0.0

    def __init__(self, initial):
        self._inner = float(initial)
        self.extract()

    def extract(self):
        self._outer = self._inner

    def update_value(self, new_value):
        self._inner = new_value

    def get_inner(self):
        return self._inner

    def get_outer(self):
        return self._outer
