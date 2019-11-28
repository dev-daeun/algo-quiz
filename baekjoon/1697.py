from sys import stdin


N, K = list(map(int, stdin.readline().split()))

MAX_AMOUNT = 2 * 100000
visited = [False for _ in range(MAX_AMOUNT+1)]
dist = [0 for _ in range(MAX_AMOUNT+1)]


def adjacent_list(v):
    return (
        v - 1,
        v + 1,
        v * 2,
    )


'''
BFS: 정점을 모두 1번씩만 방문하여 경로를 구한다.

1. 문제에서 원하는 최소 비용이 두 정점의 거리이고, 
2. 간선의 가중치가 모두 동일할 때

BFS를 이용하여 최단거리를 구할 수 있다.
'''


def bfs():
    queue = list()
    queue.append(N)

    while queue:
        x = queue.pop(0)
        if x == K:
            return dist[x]
        for next_v in adjacent_list(x):
            if 0 <= next_v <= MAX_AMOUNT:
                if not visited[next_v]:
                    visited[next_v] = True
                    dist[next_v] = dist[x] + 1
                    queue.append(next_v)

    return dist[K]


def get_answer():
    print(bfs())


get_answer()
