from itertools import permutations
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().strip('\n').split()))

# 수열을 사전순으로 나열하려면 permutations()에 넘겨지는 iterable이 사전순으로 정렬되어 있어야 한다.
sorted_numbers = sorted(numbers)

perms = permutations(sorted_numbers, M)
for p in perms:
    print(' '.join([str(e) for e in p]))
