from matplotlib.pyplot import quiver
import numpy as np


class SpanningTree():
    """ Spanning Tree class """

    def __init__(self, nodes, edges, min_count, quiet=False):
        self.nodes = nodes
        self.edges = edges
        self.min_count = min_count
        self.quiet = quiet

    def gen(self):
        """ Generate the spanning tree """
        counts = np.array([n.count for n in self.nodes])

        while np.min(counts) < self.min_count:
            r = np.random.choice(self.nodes, 1)[0]

            if self.quiet is False:
                print(f"\n--- Next iteration ---\nRandom node selected: {r.name} (count: {r.count})")

            for e in self.edges:
                if r.name == e.start:
                    if r.root == e.end:
                        if self.quiet is False:
                            print(f"Edge {r.name} >> {e.end}: Edge leads to the root of {r.name}")
                        continue

                    next_node = self.get_node_by_name(e.end)
                    if next_node.root > r.root:
                        next_node.root = r.root
                        next_node.cost = (r.cost+e.cost)
                        next_node.next_node = r.name
                        if self.quiet is False:
                            print(f"Edge {r.name} >> {e.end}: ROOT-ID of {r.name} is lower: Override the root information of {next_node.name}")
                    elif next_node.root == r.root:
                        if next_node.cost > (r.cost+e.cost):
                            next_node.cost = r.cost+e.cost
                            next_node.next_node = r.name
                            if self.quiet is False:
                                print(f"Edge {r.name} >> {e.end}: ROOT-ID of {r.name} is equals and the costs are lower: Override the cost and next_node information of {next_node.name}")

            r.count += 1
            counts = np.array([n.count for n in self.nodes])

        if self.quiet is False:
            print("\n--- Finished ---\nAll nodes has sent the minimal amount of messages.")

    def get_node_by_name(self, name):
        for n in self.nodes:
            if n.name == name:
                return n

    def get_node_by_id(self, nodeid):
        for n in self.nodes:
            if n.nodeid == nodeid:
                return n
