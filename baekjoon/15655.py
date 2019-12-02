from itertools import combinations
from sys import stdin

N, M = list(map(int, stdin.readline().split()))
numbers = list(map(int, stdin.readline().strip('\n').split()))


'''
조건: 
 1. N개의 자연수 중에서 M개를 고른 수열.
 2. 고른 수열은 오름차순이어야 한다.

주어진 숫자리스트에서 M개를 선택하여 정렬하면 됨. => 순열이 필요하지 않고 조합을 사용한다.

수열을 사전순으로 나열하려면 combinations()에 넘겨지는 iterable이 사전순으로 정렬되어 있어야 한다.
'''
sorted_numbers = sorted(numbers)
coms = combinations(sorted_numbers, M)

for c in coms:
    nums = sorted(c)
    print(' '.join([str(e) for e in nums]))
