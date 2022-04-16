class Node():
    """ Class for a node """
    def __init__(self, name, nodeid) -> None:
        self.name = name
        self.nodeid = nodeid
        self.root = self.nodeid
        self.next_node = 0
        self.cost = 0
        self.count = 0