from itertools import permutations
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().strip('\n').split()))


perms = permutations(sorted(numbers), M)
unique_perms = sorted(set(perms))

for c in unique_perms:
    print(' '.join([str(e) for e in c]))
