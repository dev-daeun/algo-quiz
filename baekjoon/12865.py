from sys import stdin

N, W = list(map(lambda x: int(x), stdin.readline().split()))


class Thing:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight


things = []
for _ in range(N):
    w, v = list(map(lambda x: int(x), stdin.readline().split()))
    things.append(Thing(val=v, weight=w))

values = []
for _ in range(N):
    values.append([0 for _ in range(W+1)])

for i in range(1, N):
    for w in range(1, W+1):
        if things[i].weight <= w:
            values[i][w] = max(values[i-1][w], values[i-1][W-things[i].weight] + things[i].val)

print(values[N-1][W])
