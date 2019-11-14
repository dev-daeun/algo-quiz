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


'''
(i, j)번째 칸은 i * M + j 로 식별가능함. 예) N = 4, M = 4 일 때 각 칸은

00 01 02 03
04 05 06 07
08 09 10 11
12 13 14 15

으로 표현 가능.

각 칸은 가로로 자른 조각(width_set) 또는 세로로 자른 조각(height_set) 중 하나에 속함. -> 집합의 경우의 수 = pow(2, N * M)
예)
- - | -
- | | |
| - - -
| | - -

위의 경우 width_set = (0, 1, 3, 4, 9, 10, 11, 14, 15), height_set = (2, 5, 6, 7, 8, 12, 13)

길이가 n인 조각을 n자리 수로 나타내므로, 각 집합의 합계를 구할 때에는 가로/세로로 이어진 조각의 칸이 나올 때마다 10씩 곱해서 더한다.
'''


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
