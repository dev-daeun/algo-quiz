from sys import stdin

N, W = list(map(lambda x: int(x), stdin.readline().split()))


class Thing:
    def __init__(self, val, weight):
        self.val = val
        self.weight = weight


# 1-index based
things = [Thing(val=0, weight=0)]
for _ in range(N):
    w, v = list(map(lambda x: int(x), stdin.readline().split()))
    things.append(Thing(val=v, weight=w))

# * Knapsack without repetition *
# values(i, w) : 배낭에 w 무게만큼의 물건이 있을 때 (1, 2, ... i)번째 까지의 물건들로 구성할 수 있는 최적의 가치
values = []
for _ in range(N+1):
    values.append([0 for _ in range(W+1)])

for i in range(1, N+1):
    for w in range(1, W+1):
        if things[i].weight <= w:
            # i번째 물건을 넣지 않을 때의 가치와 i번째 물건을 넣었을 때의 가치 중 최대값을 선택
            values[i][w] = max(values[i-1][w], values[i-1][w-things[i].weight] + things[i].val)
        else:
            values[i][w] = values[i-1][w]

print(values[N][W])


# Test 1
# 5 10
# 1 1
# 1 2
# 1 3
# 1 4
# 1 5
# expected answer: 15


# Test 2
# 4 3
# 6 13
# 4 8
# 3 6
# 5 12
# expected answer: 6
