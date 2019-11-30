from sys import stdin

M, N = list(map(int, stdin.readline().split()))

maze = list()
visited = list()
broken = list()
for _ in range(N):
    maze.append(list(stdin.readline().strip('\n')))
    visited.append([False for _ in range(M)])
    broken.append([0 for _ in range(M)])


def adjacent_list(x, y):
    return (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
    )


'''
broken[i]: i번째 정점을 방문했을 때 기준으로 부순 벽의 갯수


인접한 정점이 

1) 벽일 때: 인접한 정점의 값을 0으로 변경하고 broken[next_v] = broken[x] + 1 처리한다. 이 때 next_v와 x의 간선의 거리는 1인 것과 같다.
2) 방일 때: broken[next_v] = broken[x]. 이 때 next_v와 x의 간선의 거리는 0인 것과 같다.

=> BFS + Dequeue 사용해야 함.
'''


def bfs():
    init_x, init_y = 0, 0

    dequeue = list()
    dequeue.append((init_x, init_y))
    visited[init_x][init_y] = True

    while dequeue:
        x, y = dequeue.pop(0)
        if x == N - 1 and y == M - 1:
            return broken[x][y]

        for next_x, next_y in adjacent_list(x, y):
            if 0 <= next_x < N and 0 <= next_y < M:
                if not visited[next_x][next_y]:
                    if maze[next_x][next_y] == '1':
                        maze[next_x][next_y] = '0'
                        broken[next_x][next_y] = broken[x][y] + 1
                        dequeue.append((next_x, next_y))
                    else:
                        broken[next_x][next_y] = broken[x][y]
                        dequeue.insert(0, (next_x, next_y))

                    visited[next_x][next_y] = True

    return broken[N-1][M-1]


print(bfs())
