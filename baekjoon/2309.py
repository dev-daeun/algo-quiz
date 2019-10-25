import itertools
import sys

heights = []
for _ in range(9):
    heights.append(int(input()))

permutations = itertools.combinations(heights, 7)

for p in permutations:
    if sum(p) == 100:
        print(sorted(p))
        sys.exit()
