from sys import stdin


def find(parent, name):
    x = name
    while parent[x] != x:
        x = parent[x]
    parent[name] = x
    return x


def union(parent, size_of_net, rank, name1, name2):
    p1 = parent.get(name1)
    if not p1:
        parent[name1] = name1
        size_of_net[name1] = 1
        rank[name1] = 0

    p2 = parent.get(name2)
    if not p2:
        parent[name2] = name2
        size_of_net[name2] = 1
        rank[name2] = 0

    p1_root = find(parent, name1)
    p2_root = find(parent, name2)

    if p1_root == p2_root:
        return size_of_net[p1_root]

    if rank[p1_root] > rank[p2_root]:
        parent[p2_root] = p1_root
        size_of_net[p1_root] += size_of_net[p2_root]
        return size_of_net[p1_root]
    else:
        parent[p1_root] = p2_root
        size_of_net[p2_root] += size_of_net[p1_root]
        if rank[p1_root] == rank[p2_root]:
            rank[p2_root] += 1
        return size_of_net[p2_root]


NUM_OF_TESTS = int(stdin.readline().split()[0])
results = []
for _ in range(NUM_OF_TESTS):
    N = int(stdin.readline().split()[0])
    parent = {}
    size_of_net = {}
    rank = {}
    for _ in range(N):
        name1, name2 = stdin.readline().split()
        results.append(union(parent, size_of_net, rank, name1, name2))

for r in results:
    print(r)
