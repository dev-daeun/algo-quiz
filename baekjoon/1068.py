from sys import stdin


N = int(stdin.readline())
parents = list(map(int, stdin.readline().strip('\n').split()))
node_to_delete = int(stdin.readline())


class Node:
    def __init__(self, val):
        self.val = val
        self.children = list()
        self.deleted = False


def delete_node(node):
    node.deleted = True
    if not node.children:
        return
    
    for child in node.children:
        delete_node(child)


def get_answer():
    nodes = [Node(i) for i in range(N)]
    
    for i, p in enumerate(parents):
        if p == -1:
            continue
        nodes[p].children.append(nodes[i])

    delete_node(nodes[node_to_delete])

    num_of_leaf = 0
    for i in range(N):
        if not nodes[i].deleted and not nodes[i].children:
            num_of_leaf += 1
    
    return num_of_leaf


print(get_answer())
