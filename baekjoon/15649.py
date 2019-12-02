from itertools import permutations
from sys import stdin

N, M = list(map(int, stdin.readline().split()))

perms = permutations(range(1, N+1), M)
for p in perms:
    print(' '.join([str(e) for e in p]))
