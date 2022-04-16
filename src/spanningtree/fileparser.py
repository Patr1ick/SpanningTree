import numpy as np
from .edge import Edge
from .node import Node


class FileParser():
    """ Parser to parse a file """

    def __init__(self, path):
        """
        Parameters
        --- 
        path: str
            Path to the file to parse
        """
        with open(path) as f:
            lines = f.readlines()

        self.lines = lines

    def isNodeInList(self, name, nodes_list):
        for n in nodes_list:
            if n.name == name:
                return True
        return False

    def isEdgeInList(self, start, end, edge_list):
        for e in edge_list:
            if e.start == start and e.end == end:
                return True
        return False

    def parse(self, return_value=False):
        """ Parse the file """
        nodes = []

        edges = []

        for l in self.lines:
            if '//' in l:
                continue
            elif '=' in l:  # Nodes
                # Replace all whitespaces
                l = l.replace(' ', '').replace(';', '').replace('\n', '')
                # Split the string by the =
                l = l.split('=')

                # Check if the node already exists
                if self.isNodeInList(l[0], nodes) is False:
                    # Add the data to lists
                    n = Node(l[0], int(l[1]))

                    nodes.append(n)
                continue
            elif ':' in l:  # Edges
                # Replace all whitespaces
                l = l.replace(' ', '').replace(';', '').replace('\n', '')
                # Split the string by : to get the costs
                l = l.split(':')
                cost = int(l[1])
                # Split the string
                l = l[0].split('-')

                # Check if edge is already in list and does not connect a node with itself
                if self.isEdgeInList(l[0], l[1], edges) is False and (l[0] != l[1]):
                    e1 = Edge(l[0], l[1], cost)
                    e2 = Edge(l[1], l[0], cost)

                    edges.append(e1)
                    edges.append(e2)
            else:
                continue

        self.nodes = np.array(nodes)
        self.edges = np.array(edges)

        if return_value:
            return self.nodes, self.edges