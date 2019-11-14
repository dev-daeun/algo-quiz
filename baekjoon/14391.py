from sys import stdin

N, M = list(map(int, stdin.readline().split()))
P = list()
for _ in range(N):
    row = list(stdin.readline().strip('\n'))
    P.append(row)


def calculate_width_sum(width_set):
    total_sum = 0
    for i in range(N):
        cur_sum = 0
        exp = 0
        for j in range(M-1, -1, -1):
            n = i * M + j
            if (1 << n) & width_set:
                cur_sum += pow(10, exp) * int(P[i][j])
                exp += 1
            else:
                total_sum += cur_sum
                exp = 0
                cur_sum = 0
        total_sum += cur_sum
    return total_sum


def calculate_height_sum(height_set):
    total_sum = 0
    for j in range(M):
        cur_sum = 0
        exp = 0
        for i in range(N-1, -1, -1):
            n = i * M + j
            if (1 << n) & height_set:
                cur_sum += pow(10, exp) * int(P[i][j])
                exp += 1
            else:
                total_sum += cur_sum
                exp = 0
                cur_sum = 0
        total_sum += cur_sum
    return total_sum


def get_answer():
    answer = 0
    u = (1 << (N * M)) - 1
    for width_set in range(1 << (N * M)):
        height_set = u - width_set
        width_sum = calculate_width_sum(width_set)
        height_sum = calculate_height_sum(height_set)
        answer = max(answer, width_sum + height_sum)

    return answer


print(get_answer())
