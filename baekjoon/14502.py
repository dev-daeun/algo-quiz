import copy

from itertools import permutations
from sys import stdin


ROOM = '0'
WALL = '1'
VIRUS = '2'
NUM_OF_WALLS = 3


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
    is_pushed = False

    while stack:
        x, y = stack[-1]
        print(f"{x} {y}")
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

    three_wall_cases = permutations(cells_to_be_wall, NUM_OF_WALLS)
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


print(get_answer())
