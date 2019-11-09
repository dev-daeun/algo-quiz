from sys import stdin
from itertools import permutations

N = int(stdin.readline())
W = list()
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    W.append(row)


def total_cost_per_path(perm):
    total_cost = 0
    for i in range(len(perm)):
        if i == len(perm) - 1:
            cost = W[perm[i]][perm[0]]
        else:
            cost = W[perm[i]][perm[i+1]]
        
        if cost == 0:
            return None
        total_cost += cost
    
    return total_cost

perms = permutations(range(N))
nominates = list()
for p in perms:
    total_cost = total_cost_per_path(p)
    if total_cost:
        nominates.append(total_cost)

answer = min(nominates)
print(answer)

# 시간복잡도 : N * N!
# 제출할 때 언어 선택을 python3으로 하면 시간초과나고 pypy로 하면 통과됨...뭐야...
