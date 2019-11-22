from sys import stdin

N, M = list(map(int, stdin.readline().split()))

pan = list()
for _ in range(N):
    row = list(stdin.readline().strip('\n'))
    pan.append(row)

visited = list()
cnt = list()
for _ in range(N):
    visited.append([False for _ in range(M)])
    cnt.append([0 for _ in range(M)])


def adjacent_cells(x, y):
    return (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    )


def dfs(init_x, init_y):
    stack = list()
    stack.append((init_x, init_y))
    visited[init_x][init_y] = True

    while stack:
        x, y = stack[-1]
        is_pushed = False
        for next_x, next_y in adjacent_cells(x, y):
            if 0 <= next_x < N and 0 <= next_y < M:
                if pan[next_x][next_y] == pan[x][y]:
                    if not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        cnt[next_x][next_y] = cnt[x][y] + 1
                        stack.append((next_x, next_y))
                        is_pushed = True
                        break
                    else:
                        if cnt[next_x][next_y] - cnt[x][y] >= 3:
                            return True
        if not is_pushed:
            stack.pop(-1)

    return False


def get_answer():
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                result = dfs(i, j)
                if result:
                    return 'Yes'
    return 'No'


print(get_answer())
