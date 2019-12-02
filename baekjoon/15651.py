from itertools import product
from sys import stdin

N, M = list(map(int, stdin.readline().split()))


'''
조건:
 1. 1부터 N까지 자연수 중에서 M개를 고른 수열.
 2. 같은 수를 여러 번 골라도 된다.


N개의 숫자 중에 M개를 중복으로 선택하여 순서를 매긴다. => 숫자리스트를 M번의 cartesian product 하여 해결 가능함.
itertools.product(iterable[, repeat]) 사용.

https://docs.python.org/2/library/itertools.html#itertools.product
'''
cartesians = product(range(1, N + 1), repeat=M)
for c in cartesians:
    print(' '.join([str(e) for e in c]))
