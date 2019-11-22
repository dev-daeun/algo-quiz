from sys import stdin

N, M = list(map(int, stdin.readline().split()))

pan = list()
for _ in range(N):
    row = list(stdin.readline().strip('\n'))
    pan.append(row)

visited = list()
dist = list()
for _ in range(N):
    visited.append([False for _ in range(M)])
    dist.append([0 for _ in range(M)])


def adjacent_cells(x, y):
    return (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    )


'''
** 그래프에서 사이클을 찾는다. => DFS로 해결한다. **

방문 가능한 정점: 시작 정점과 색이 같고 visited = False 인 정점

1) 정점을 방문할 때 마다 시작정점 ~ 방문정점 사이의 거리를 저장한다.
2) 어떤 정점과 인접한 정점들 중에 이미 방문한 정점이 있을 경우, 두 정점의 거리의 차가 3이상이면 cycle이 있다고 본다.

예)
A - B
|   |
D - C

A가 시작점일 때 방문 순서: A B C D

dist[A] = 0
dist[B] = dist[A] + 1 = 1
dist[C] = dist[B] + 1 = 2
dist[D] = dist[C] + 1 = 3 

==> dist[D] - dist[A] = 3 - 0 = 3
'''
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
                        dist[next_x][next_y] = dist[x][y] + 1
                        stack.append((next_x, next_y))
                        is_pushed = True
                        break
                    else:
                        if dist[next_x][next_y] - dist[x][y] >= 3:
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
