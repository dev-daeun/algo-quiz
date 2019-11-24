from sys import stdin


N = int(stdin.readline())
parents = list(map(int, stdin.readline().strip('\n').split()))
node_to_delete = int(stdin.readline())


class Node:
    def __init__(self, val):
        self.val = val
        self.children = list()
        self.deleted = False


# 어떤 노드를 삭제할 때 그 노드의 자손 노드들까지 재귀적으로 deleted = True 처리한다.
def delete_node(node):
    node.deleted = True
    if not node.children:
        return
    
    for child in node.children:
        delete_node(child)


# 자식이 아예 없거나 자식이 있을 때 모두 deleted = True 처리된 경우 그 노드는 leaf 노드에 해당한다.
def is_leaf(node):
    if not node.children:
        return True

    for child in node.children:
        if not child.deleted:
            return False
    return True


def get_answer():
    nodes = [Node(i) for i in range(N)]
    
    for i, p in enumerate(parents):
        if p == -1:
            continue
        nodes[p].children.append(nodes[i])

    delete_node(nodes[node_to_delete])

    num_of_leaf = 0
    for i in range(N):
        if not nodes[i].deleted and is_leaf(nodes[i]):
            num_of_leaf += 1
    
    return num_of_leaf


print(get_answer())
