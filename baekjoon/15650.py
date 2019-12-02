from itertools import combinations
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
coms = combinations(range(1, N + 1), M)


'''
조건:
 1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
 2. 고른 수열은 오름차순이어야 한다.
 
N개의 숫자 중에서 M개의 숫자를 선택한 뒤에, 정렬하면 됨. => 순열이 필요하지 않고 조합을 사용한다.
'''
for c in coms:
    nums = sorted(c)
    print(' '.join([str(e) for e in nums]))
