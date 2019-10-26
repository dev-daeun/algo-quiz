class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self


class DynamicConnectivity:
    # class takes the number of objects n as input,
    # and initializes a data structure with objects numbered from
    # 0 to N-1
    def __init__(self, n):
        self.nodes = [Node(val=i) for i in range(n)]

    def find(self, p):
        p = self.nodes[p]
        x = p
        while x != x.parent:
            x = x.parent
        p.parent = x
        return p.parent

    # union connects point p with point q
    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return

        if p_root.rank > q_root.rank:
            q_root.parent = p_root
        else:
            p_root.parent = q_root
            if p_root.rank == q_root.rank:
                q_root.rank += 1

    # connected checks if point p is connected to point q and returns a boolean
    def connected(self, p, q):
        return self.find(p) == self.find(q)
