from sys import stdin

N, M, V = list(map(int, stdin.readline().split()))

# 인접행렬 구현
adjacent_matrix = list()
for _ in range(N):
    adjacent_matrix.append([False for _ in range(N)])

for _ in range(M):
    v1, v2 = list(map(int, stdin.readline().split()))
    adjacent_matrix[v1-1][v2-1] = True
    adjacent_matrix[v2-1][v1-1] = True


# 재귀가 아닌 스택으로 dfs 구현
def dfs(init):
    visited = [False for _ in range(N)]

    stack = list()
    stack.append(init - 1)

    result = list()
    result.append(init)
    visited[init-1] = True

    while stack:
        x = stack[-1]
        nomi_list = list()
        for i in range(N):
            if not visited[i] and adjacent_matrix[i][x]:
                nomi_list.append(i)

        if nomi_list:
            next_x = min(nomi_list)
            visited[next_x] = True
            result.append(next_x + 1)
            stack.append(next_x)
        else:
            stack.pop(-1)

    return result


def bfs(init):
    visited = [False for _ in range(N)]

    queue = list()
    queue.append(init - 1)
    visited[init-1] = True
    result = list()

    while queue:
        x = queue.pop(0)
        result.append(x + 1)
        for i in range(N):
            if not visited[i] and adjacent_matrix[i][x]:
                visited[i] = True
                queue.append(i)

    return result


def get_answer():
    dfs_result = dfs(V)
    bfs_result = bfs(V)
    print(' '.join([str(e) for e in dfs_result]))
    print(' '.join([str(e) for e in bfs_result]))


get_answer()
