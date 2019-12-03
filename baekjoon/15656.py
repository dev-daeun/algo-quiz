from itertools import product
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().split()))

sorted_numbers = sorted(numbers)

cartesian = product(sorted_numbers, repeat=M)
for c in cartesian:
    print(' '.join([str(e) for e in c]))
