class Node:
    # index is the space in maze
    index = None

    # value is the value of the space
    value = None

    def __init__(self, index, value, e_val='z'):
        self.index = index
        self.value = value
        self.e_val = e_val

    def __hash__(self):
        return self.index

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.index == other.index
        return NotImplemented

    def __str__(self):
        return "[{}.{}]".format(self.index, self.value)

    def __repr__(self):
        return "[{}.{}]".format(self.index, self.value)

    def get_clean_value(self):
        if self.value == 'S':
            return 'a'

        if self.value == 'E':
            return self.e_val

        return self.value

    # return True if the self node can proceed forward to the other node
    def can_step_to(self, other_node):
        # we can step to an equal
        # or one greater
        # or any less

        our_level = ord(self.get_clean_value())
        their_level = ord(other_node.get_clean_value())

        if our_level == their_level:
            return True

        if our_level > their_level:
            return True

        if our_level + 1 == their_level:
            return True

    # return True if the self node is a "back" node of the other node. This means the other node can step to this node
    def is_a_back_of(self, other_node):
        return other_node.can_step_to(self)

    def add_connection(self, node):
        if not self.b_paths.__contains__(node):
            self.f_paths.add(node)
            node.b_paths.add(self)


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        # '''
        # This method makes sure that the graph is symmetrical. In other words,
        #  if there's a path from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        # '''
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        # for node, edges in graph.items():
        #     for adjacent_node, value in edges.items():
        #         if not graph[adjacent_node].get(node, False):
        #             graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]
