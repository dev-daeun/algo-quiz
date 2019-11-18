from sys import stdin

N, M = list(map(int, stdin.readline().split()))

visited = [False for _ in range(N)]

adjacent_list = list()
for _ in range(N):
    adjacent_list.append(list())

for _ in range(M):
    u, v = list(map(int, stdin.readline().split()))
    adjacent_list[u-1].append(v-1)
    adjacent_list[v-1].append(u-1)


def bfs(init):
    queue = list()
    queue.append(init)
    visited[init] = True

    while queue:
        x = queue.pop(0)
        for v in adjacent_list[x]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)


def get_answer():
    cnt = 0
    while True:
        unvisited_list = list()

        for i in range(N):
            if not visited[i]:
                unvisited_list.append(i)

        if unvisited_list:
            init_v = unvisited_list[0]
            bfs(init_v)
            cnt += 1
        else:
            print(cnt)
            return


get_answer()
