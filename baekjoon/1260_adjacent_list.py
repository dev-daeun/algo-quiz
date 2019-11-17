from sys import stdin

N, M, V = list(map(int, stdin.readline().split()))

# 인접리스트 구현
adjacent_list = [list() for _ in range(N)]
for _ in range(M):
    v1, v2 = list(map(int, stdin.readline().split()))
    adjacent_list[v1-1].append(v2)
    adjacent_list[v2-1].append(v1)


dfs_result = list()
bfs_result = list()


def dfs(init, visited):
    visited[init-1] = True
    dfs_result.append(init)
    for v in sorted(adjacent_list[init-1]):
        if not visited[v-1]:
            dfs(v, visited)


def bfs(init, visited):
    queue = list()
    queue.append(init)

    visited[init-1] = True

    while queue:
        x = queue.pop(0)
        bfs_result.append(x)
        for v in sorted(adjacent_list[x-1]):
            if not visited[v-1]:
                visited[v-1] = True
                queue.append(v)


def get_answer():
    dfs(V, visited=[False for _ in range(N)])
    bfs(V, visited=[False for _ in range(N)])

    print(' '.join([str(e) for e in dfs_result]))
    print(' '.join([str(s) for s in bfs_result]))


get_answer()
