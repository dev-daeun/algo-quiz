from sys import stdin

N = int(stdin.readline().strip('\n'))


'''
loc_of_queens[i] = i번째 열에 있는 퀸이 위치한 행

i번째 열에 i번째 퀸을 놓는 경우의 수 = i번째 열의 0 ~ (N - 1)번째 행에 퀸을 놓는 경우의 수

0 ~ (N - 1)을 순회하면서 0 ~ (i - 1)번째에 이미 위치한 퀸들과 충돌하지 않다면(promising 하다면)

(i + 1)번째 열에 퀸을 놓는 방법을 탐색한다. (n_queen(i+1)을 호출한다.) 

promising 하지 않은 경우는 추가적인 재귀호출을 하지 않으므로 pruning 처리된다.


* 푸는 데 시간 오래걸린 이유 *
 다음 퀸을 놓을 수 있는 칸을 구하는 로직(adjacent_list 구하는 방법)이 잘못됨.
 두 퀸이 같은 대각선에 있는지 검사하는 조건문이 잘못됨.
 이중 for문 안에서 n_queen()을 재귀호출해서 시간 초과 남. 
'''

answer = 0
loc_of_queens = [0 for _ in range(N)]


def is_promising(prev_col):
    # 이전에 이미 놓아진 퀸들을 순회하면서 각각의 이전 퀸이 최근 퀸과 충돌하는지 검사한다.
    # 같은 행에 있거나 같은 대각선에 위치하면 promising 하지 않다.
    for col in range(prev_col):
        if loc_of_queens[col] == loc_of_queens[prev_col] or abs(loc_of_queens[col] - loc_of_queens[prev_col]) == abs(col - prev_col):
            return False
    return True


def n_queen(prev_col):
    global answer
    if prev_col == N:
        answer += 1
        return

    for i in range(N):
        loc_of_queens[prev_col] = i
        if is_promising(prev_col):
            n_queen(prev_col+1)


def get_answer():
    n_queen(0)
    print(answer)


get_answer()
