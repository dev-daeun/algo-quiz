from sys import stdin
from itertools import permutations

N = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))

perms = permutations(nums)
answer = 0
for p in perms:
    sum_ = 0
    for i in range(1, N):
        sum_ += abs(p[i] - p[i-1])
    answer = max(answer, sum_)

print(answer)
