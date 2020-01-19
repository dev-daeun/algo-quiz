from heapq import heappop, heappush, heapify
from sys import stdin, maxsize


def relax(v, adj_v, w, dist):
    if dist[adj_v] > dist[v] + w:
        dist[adj_v] = dist[v] + w
        return True
    return False


def dijkstra(start, adjacent_list, n):
    dist = [INF for _ in range(n)]
    dist[start] = 0

    q = list()
    heapify(q)
    heappush(q, (dist[start], start))

    while q:
        dist_v, v = heappop(q)
        for adj_v, adj_w in adjacent_list[v]:
            is_relaxed = relax(v, adj_v, adj_w, dist)
            if is_relaxed:
                heappush(q, (dist[adj_v], adj_v))

    return dist


INF = maxsize

n, m = list(map(int, stdin.readline().split()))
start = int(stdin.readline().strip('\n'))
start -= 1  # 0-index based

adjacent_list = [list() for _ in range(n)]
for _ in range(m):
    v1, v2, w = list(map(int, stdin.readline().split()))
    adjacent_list[v1-1].append((v2 - 1, w))

result = dijkstra(start, adjacent_list, n)

for i in range(n):
    print('INF') if result[i] == INF else print(result[i])
