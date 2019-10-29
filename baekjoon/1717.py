from sys import stdin


class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0


def find(p):
    x = p
    while x.parent != x:
        x = x.parent
    p.parent = x
    return p.parent


def is_in_same_set(p, q):
    if find(p) == find(q):
        return 'YES'
    else:
        return 'NO'


def union(p, q):
    p_root = find(p)
    q_root = find(q)

    if p_root == q_root:
        return

    if p_root.rank > q_root.rank:
        q_root.parent = p_root
    else:
        p_root.parent = q_root
        if p_root.rank == q_root.rank:
            q_root.rank += 1


N, M = list(map(lambda x: int(x), stdin.readline().split()))
inputs = [Node(val=i) for i in range(N+1)]

answers = []
for _ in range(M):
    op, a, b = list(map(lambda x: int(x), stdin.readline().split()))

    if op == 0:
        union(inputs[a], inputs[b])
    if op == 1:
        answers.append(is_in_same_set(inputs[a], inputs[b]))

for a in answers:
    print(a)
