from sys import stdin


class Node:
    def __init__(self, name):
        self.parent = self
        self.name = name
        self.num_of_friends = 1
        self.rank = 0


def find(p):
    x = p
    while x != x.parent:
        x = p.parent
    p.parent = x
    return x


def union(people, name1, name2):
    p1 = people.setdefault(name1, Node(name=name1))
    p2 = people.setdefault(name2, Node(name=name2))

    p1_root = find(p1)
    p2_root = find(p2)

    if p1_root == p2_root:
        return p1_root.num_of_friends

    if p1_root.rank > p2_root.rank:
        p2_root.parent = p1_root
        p1_root.num_of_friends += p2_root.num_of_friends
        return p1_root.num_of_friends
    else:
        p1_root.parent = p2_root
        p2_root.num_of_friends += p1_root.num_of_friends
        if p1_root.rank == p2_root.rank:
            p2_root.rank += 1
        return p2_root.num_of_friends


NUM_OF_TESTS = int(stdin.readline().split()[0])
results = []
for _ in range(NUM_OF_TESTS):
    N = int(stdin.readline().split()[0])
    people = {}
    for _ in range(N):
        name1, name2 = stdin.readline().split()
        results.append(union(people, name1, name2))

for r in results:
    print(r)
