from itertools import combinations_with_replacement
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
coms = combinations_with_replacement(range(1, N + 1), M)

'''
조건:
 1. 1부터 N까지 자연수 중에서 M개를 고른 수열
 2. 같은 수를 여러 번 골라도 된다.
 3. 고른 수열은 비내림차순이어야 한다. 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

N개의 숫자 중에서 M개의 중복으로 선택한 뒤, 정렬하면 됨. => 순열이 필요하지 않고 조합을 사용한다.

itertools.combinations_with_replacement()는 iterable에서 원소를 중복으로 선택한다.
'''
for c in coms:
    nums = sorted(c)
    print(' '.join([str(e) for e in nums]))
