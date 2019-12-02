from math import gcd
from sys import stdin


def get_answer(m, n, x, y):
    if x == y:
        return x

    lcm = m * n / gcd(m, n)  # m과 n의 최소공배수. 카잉 달력의 마지막 해는 (m, n의 최소공배수)번째에 해당한다.
    i = 1
    while True:
        offset = x + M * i  # x를 기준으로 달력을 건너뛴다.
        if offset > lcm:    # offset이 가장 마지막 해의 순서보다 크면 유효하지 않은 입력이므로 -1을 리턴한다.
            return -1

        if offset % n == y:
            return offset

        i += 1


AMOUNT_OF_TESTS = int(stdin.readline().strip('\n'))
answers = list()
for _ in range(AMOUNT_OF_TESTS):
    M, N, x, y = list(map(int, stdin.readline().split()))
    answers.append(get_answer(M, N, x, y))

for ans in answers:
    print(ans)
