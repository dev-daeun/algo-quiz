from itertools import combinations_with_replacement
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().split()))

sorted_numbers = sorted(numbers)

coms = combinations_with_replacement(sorted_numbers, M)
for c in coms:
    print(' '.join([str(e) for e in c]))
