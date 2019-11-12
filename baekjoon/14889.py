from sys import maxsize, stdin

N = int(stdin.readline())

P = list()
for _ in range(N):
    P.append(list(map(int, stdin.readline().split())))


def calculate_power(s):
    power = 0
    elements = list()

    for n in range(N):
        if s & (1 << n):
            elements.append(n)

    for i in elements:
        for j in elements:
            power += P[i][j]

    return power


def get_answer():
    U = (1 << N) - 1
    answer = maxsize

    for s1 in range(1 << N):
        s2 = U - s1

        s1_cnt = 0
        s2_cnt = 0

        for n in range(N):
            if s1 & (1 << n):
                s1_cnt += 1
            else:
                s2_cnt += 1

        if s1_cnt == s2_cnt == (N / 2):
            s1_power = calculate_power(s1)
            s2_power = calculate_power(s2)
            answer = min(answer, abs(s1_power - s2_power))

    return answer


print(get_answer())
