import sys


def find_best_path_to_end(node):
    best_path = [node]

    if node.value != 'E':
        best_path_len = sys.maxsize
        for next_path_node in node.f_paths:
            candidate_path = find_best_path_to_end(next_path_node)
            if len(candidate_path) < best_path_len:
                best_path_len = len(candidate_path)
                best_path.extend(candidate_path)

    node.best_path_to_end = best_path

    return best_path

def print_node_paths(nodes):
    for node in nodes:
        print("{} : {} : {}".format(node, node.best_path_to_end, len(node.best_path_to_end) - 1))