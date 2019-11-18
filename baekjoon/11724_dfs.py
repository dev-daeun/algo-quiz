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


# 재귀 없는 dfs 구현
def dfs(init):
    stack = list()
    stack.append(init)
    visited[init] = True

    while stack:
        x = stack[-1]

        nomi_list = list()
        for v in adjacent_list[x]:
            if not visited[v]:
                nomi_list.append(v)

        if nomi_list:
            visited[nomi_list[0]] = True
            stack.append(nomi_list[0])
        else:
            stack.pop(-1)


def get_answer():
    cnt = 0
    while True:
        unvisited_list = list()

        for i in range(N):
            if not visited[i]:
                unvisited_list.append(i)

        if unvisited_list:
            init_v = unvisited_list[0]
            dfs(init_v)
            cnt += 1
        else:
            print(cnt)
            return


get_answer()
