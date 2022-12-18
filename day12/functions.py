import sys


def get_next_hops(node, matrix):
    index = node.index
    paths = []

    right = matrix.get_right(index)
    if right is not None and node.can_step_to(right):
        paths.append(right)

    left = matrix.get_left(index)
    if left is not None and node.can_step_to(left):
        paths.append(left)

    up = matrix.get_above(index)
    if up is not None and node.can_step_to(up):
        paths.append(up)

    down = matrix.get_below(index)
    if down is not None and node.can_step_to(down):
        paths.append(down)

    return paths


def find_best_path_to_end(node, matrix, visited=[]):
    best_path = [node]
    visited.append(node)

    if node.value != 'E':
        best_path_len = sys.maxsize
        forward_paths = get_next_hops(node, matrix)
        for next_path_node in forward_paths:
            if not visited.__contains__(next_path_node):
                candidate_path = find_best_path_to_end(next_path_node, matrix, visited)
                if len(candidate_path) < best_path_len:
                    best_path_len = len(candidate_path)
                    best_path.extend(candidate_path)

    node.best_path_to_end = best_path

    return best_path


# from : https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


# from : https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
def print_result_d(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    path.reverse()
    print(path)


def get_next_hops(node, matrix):
    index = node.index
    paths = {}

    right = matrix.get_right(index)
    if right is not None and node.can_step_to(right):
        paths[right] = 1

    left = matrix.get_left(index)
    if left is not None and node.can_step_to(left):
        paths[left] = 1

    up = matrix.get_above(index)
    if up is not None and node.can_step_to(up):
        paths[up] = 1

    down = matrix.get_below(index)
    if down is not None and node.can_step_to(down):
        paths[down] = 1

    return paths


def find_node(nodes, val):
    for node in nodes:
        if node.value == val:
            return node
    return None

def find_nodes_with_value(nodes, val):
    found = set()
    for node in nodes:
        if node.get_clean_value() == val:
            found.add(node)
    return found


def print_node_paths(nodes):
    for node in nodes:
        print("{} : {} : {}".format(node, node.best_path_to_end, len(node.best_path_to_end) - 1))
