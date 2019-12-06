from sys import stdin


N = int(stdin.readline().strip('\n'))

OCCUPIED = 1
NOT_OCCUPIED = 0

chess = list()
for _ in range(N):
    chess.append([NOT_OCCUPIED for _ in range(N)])


def restore_chess():
    for i in range(N):
        for j in range(N):
            chess[i][j] = NOT_OCCUPIED


def is_conflict(x, y):
    # 가로 검사
    for i in range(0, N):
        if chess[x][i] == OCCUPIED:
            return True

    # 세로 검사
    for j in range(0, N):
        if chess[j][y] == OCCUPIED:
            return True

    # 왼쪽 대각선 검사
    for k in range(1, N):
        if x - k >= 0 and y - k >= 0:
            if chess[x-k][y-k] == OCCUPIED:
                return True
        if x + k < N and y + k < N:
            if chess[x+k][y+k] == OCCUPIED:
                return True

    # 오른쪽 대각선 검사
    for k in range(1, N):
        if x - k >= 0 and y + k < N:
            if chess[x-k][y+k] == OCCUPIED:
                return True

        if x + k < N and y - k >= 0:
            if chess[x+k][y-k] == OCCUPIED:
                return True

    return False


def occupy(x, y):
    # 가로 변경
    for i in range(0, N):
        chess[x][i] = OCCUPIED

    # 세로 변경
    for j in range(0, N):
        chess[j][y] = OCCUPIED

    # 왼쪽 대각선 변경
    for k in range(1, N):
        if x - k >= 0 and y - k >= 0:
            chess[x-k][y-k] = OCCUPIED
        if x + k < N and y + k < N:
            chess[x+k][y+k] = OCCUPIED

    # 오른쪽 대각선 변경
    for k in range(1, N):
        if x - k >= 0 and y + k < N:
            chess[x-k][y+k] = OCCUPIED

        if x + k < N and y - k >= 0:
            chess[x+k][y-k] = OCCUPIED

    chess[x][y] = OCCUPIED


def adjacent_list(x, y):
    return (
        (x - 2, y + 1),
        (x + 2, y - 1),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x + 1, y + 2),
        (x - 1, y - 2),
        (x + 2, y + 1),
        (x - 2, y - 1),
    )


def is_satisfied(init_x, init_y):
    stack = list()
    stack.append((init_x, init_y))
    occupy(init_x, init_y)
    left_queens = N - 1

    while stack:
        if not left_queens:
            return True

        cur_x, cur_y = stack[-1]
        is_pushed = False

        for next_x, next_y in adjacent_list(cur_x, cur_y):
            if 0 <= next_x < N and 0 <= next_y < N:
                if chess[next_x][next_y] == NOT_OCCUPIED:
                    if not is_conflict(next_x, next_y):
                        print('called')
                        occupy(next_x, next_y)
                        stack.append((next_x, next_y))
                        is_pushed = True
                        left_queens -= 1
                        break

        if not is_pushed:
            stack.pop(-1)

    return False


def get_answer():
    answer = 0

    for i in range(N):
        for j in range(N):
            if is_satisfied(i, j):
                answer += 1
            restore_chess()

    print(answer)


get_answer()
