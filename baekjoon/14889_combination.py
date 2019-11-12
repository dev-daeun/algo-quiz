from sys import maxsize, stdin
from itertools import combinations


N = int(stdin.readline())

P = list()
for _ in range(N):
    P.append(list(map(int, stdin.readline().split())))


def calculate_power(s):
    power = 0
    for i in s:
        for j in s:
            power += P[i][j]

    return power

def get_answer():
    # s1은 N개 숫자 중 N/2개 선택한 결과.
    coms = combinations(range(N), N//2)
    answer = maxsize

    for c in coms:
        s1 = c
        s2 = list()
        # 선택된 숫자를 제외한 나머지가 s2.
        for element in range(N):
            if element not in s1:
                s2.append(element)

        s1_power = calculate_power(s1)
        s2_power = calculate_power(s2)
        answer = min(answer, abs(s1_power - s2_power))

    return answer

print(get_answer())
