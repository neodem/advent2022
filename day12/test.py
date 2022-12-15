from classes import Node
import functions

nodes = []

s = Node(0, 'S')
e = Node(20, 'E')
n1 = Node(1, 'a')
n2 = Node(2, 'b')
n3 = Node(3, 'c')

nodes.append(s)
nodes.append(e)
nodes.append(n1)
nodes.append(n2)
nodes.append(n3)

n1.add_connection(e)
n2.add_connection(n3)
n3.add_connection(e)

s.add_connection(n1)
s.add_connection(n2)

path = functions.find_best_path_to_end(s)
functions.print_node_paths(nodes)
