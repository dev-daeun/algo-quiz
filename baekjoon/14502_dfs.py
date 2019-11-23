import copy

from itertools import combinations
from sys import stdin


ROOM = '0'
WALL = '1'
VIRUS = '2'
NUM_OF_WALLS = 3

'''
3 <= ROOM의 갯수 <= 64

최대 64개의 ROOM에서 3개를 선택하여 벽으로 씀. => permutation이 아닌 combination사용.
(64 * 63 * 62) / (3 * 2 * 1) = 3 ~ 4만

1. 2차원 배열 내 ROOM에 해당하는 칸을 선택하고 WALL으로 값 변경.
2. 2차원 배열 내 VIRUS에 해당하는 칸을 탐색하면서 인접한 칸 중에 ROOM에 해당하는 칸을 VIRUS로 변경.
3. VIRUS로 전염된 배열에서 남아있는 ROOM의 수를 세어 최대값을 구한다.

1 ~ 3 과정을 각 조합마다 적용한다.

** is_pushed가 while문 바깥에 정의되어 있어서 무한루프 발생. ** 
'''
N, M = list(map(int, stdin.readline().split()))
pan = list()
visited = list()
for _ in range(N):
    row = stdin.readline().strip('\n').split()
    pan.append(row)
    visited.append([False for _ in range(M)])


def restore_visted():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False


def stand_three_walls(locations, copied_pan):
    for w in locations:
        x = w // M
        y = w % M
        copied_pan[x][y] = WALL


def adjacent_cells(x, y):
    return (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    )


def dfs(init_x, init_y, copied_pan):
    stack = list()
    stack.append((init_x, init_y))
    visited[init_x][init_y] = True

    while stack:
        x, y = stack[-1]
        is_pushed = False
        for next_x, next_y in adjacent_cells(x, y):
            if 0 <= next_x < N and 0 <= next_y < M:
                if copied_pan[next_x][next_y] == ROOM and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    copied_pan[next_x][next_y] = VIRUS
                    stack.append((next_x, next_y))
                    is_pushed = True
                    break
        if not is_pushed:
            stack.pop(-1)
 

def get_answer():
    answer = 0
    cells_to_be_wall = list()
    for i in range(N):
        for j in range(M):
            if pan[i][j] == '0':
                cells_to_be_wall.append(i * M + j)

    three_wall_cases = combinations(cells_to_be_wall, NUM_OF_WALLS)
    for three_walls in three_wall_cases:
        copied_pan = copy.deepcopy(pan)
        stand_three_walls(three_walls, copied_pan)

        for i in range(N):
            for j in range(M):
                if copied_pan[i][j] == VIRUS and not visited[i][j]:
                    dfs(i, j, copied_pan)
        
        num_of_rooms = 0
        for i in range(N):
            for j in range(M):
                if copied_pan[i][j] == ROOM:
                    num_of_rooms += 1

        answer = max(answer, num_of_rooms)
        restore_visted()
        del copied_pan

    return answer


print(get_answer())
