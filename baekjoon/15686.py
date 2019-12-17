from itertools import combinations
from sys import stdin, maxsize


N, M = list(map(int, stdin.readline().split(' ')))
cells = list()
visited = list()
for _ in range(N):
    cells.append(list(map(int, stdin.readline().strip('\n').split(' '))))
    visited.append([False for _ in range(N)])


EMPTY = 0
HOME = 1
CHICK = 2


def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def adjacent_list(x, y):
    result = list()
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            else:
                result.append((x + i, y + j))
    return result


def get_chicken_dist(init_x, init_y):
    queue = list()
    queue.append((init_x, init_y))
    visited[init_x][init_y] = True

    while queue:
        x, y = queue.pop(0)
        answer = maxsize
        for next_x, next_y in adjacent_list(x, y):
            if 0 <= next_x < N and 0 <= next_y < N:
                if not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    if cells[next_x][next_y] == CHICK:
                        answer = min(answer, get_dist(init_x, init_y, next_x, next_y))
                    queue.append((next_x, next_y))
        if answer != maxsize:
            return answer

    return get_dist(init_x, init_y, x, y)


def get_total_chicken_dist():
    result = 0

    for x in range(N):
        for y in range(N):
            if cells[x][y] == HOME:
                result += get_chicken_dist(x, y)
                restore_visited()

    return result


def turn_chick_to_empty(chosen_chicks):
    chicks_to_change = list()

    for x in range(N):
        for y in range(N):
            if cells[x][y] == CHICK and (x, y) not in chosen_chicks:
                chicks_to_change.append((x, y))
                cells[x][y] = EMPTY

    return chicks_to_change


def restore_chickens(excluded_chicks):
    for x, y in excluded_chicks:
        cells[x][y] = CHICK


def restore_visited():
    for x in range(N):
        for y in range(N):
            visited[x][y] = False


def get_answer():
    chickens = list()
    for x in range(N):
        for y in range(N):
            if cells[x][y] == CHICK:
                chickens.append((x, y))

    answer = maxsize
    coms = combinations(chickens, M)
    for chosen_chicks in coms:
        excluded_chicks = turn_chick_to_empty(chosen_chicks)
        answer = min(answer, get_total_chicken_dist())
        restore_chickens(excluded_chicks)

    return answer


print(get_answer())
