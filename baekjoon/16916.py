from sys import stdin

S = stdin.readline().strip('\n')
P = stdin.readline().strip('\n')

# rabin-karp 알고리즘을 직접 구현하면 시간 초과가 난다.
# cpython built-in 이라 빠른 듯.
print(1) if P in S else print(0)
