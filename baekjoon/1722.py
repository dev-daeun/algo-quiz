import itertools
from sys import stdin

N = int(stdin.readline())

# create permutations
permutations = list(itertools.permutations(range(1, N + 1)))

# receive inputs
op, *inputs = list(map(lambda x: int(x), stdin.readline().split()))

# 0-index based
if op == 1:
    p = permutations[inputs[0]-1]
    print(' '.join([str(n) for n in p]))
else:
    print(permutations.index(tuple(inputs)) + 1)
