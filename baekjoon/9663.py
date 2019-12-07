from sys import stdin, setrecursionlimit

N = int(stdin.readline().strip('\n'))


'''
loc_of_queens[i] = i번째 열에 있는 퀸이 위치한 행
'''

answer = 0
loc_of_queens = [0 for _ in range(N)]


def is_promising(prev_col, cur_row):
    for col in range(prev_col + 1):
        if loc_of_queens[col] == cur_row or abs(loc_of_queens[col] - cur_row) == abs(col - (prev_col + 1)):
            return False
    return True


def n_queen(prev_col):
    global answer
    if prev_col == N - 1:
        answer += 1
        return

    for i in range(N):
        if is_promising(prev_col, i):
            loc_of_queens[prev_col+1] = i
            n_queen(prev_col+1)


def get_answer():
    global loc_of_queens
    for x in range(N):
        loc_of_queens[0] = x
        n_queen(0)
        loc_of_queens = [0 for _ in range(N)]

    print(answer)


get_answer()
