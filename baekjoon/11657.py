from sys import stdin, maxsize


def relax(v, adj_v, w, dist):
    if dist[adj_v] > dist[v] + w:
        dist[adj_v] = dist[v] + w
        return True
    return False


def bellman_ford(n, start, edges):
    dist = [maxsize for _ in range(n)]
    dist[start] = 0

    for _ in range(n-1):
        for v1, v2, w in edges:
            relax(v1, v2, w, dist)

    for v1, v2, w in edges:
        if relax(v1, v2, w, dist):
            return True, -1

    for idx, val in enumerate(dist):
        if val == maxsize:
            dist[idx] = -1

    return False, dist


n, m = list(map(int, stdin.readline().split()))
edges = list()
for _ in range(m):
    v1, v2, w = list(map(int, stdin.readline().split()))
    edges.append((v1 - 1, v2 - 1, w))

is_negative_cycle, dist = bellman_ford(n, 0, edges)
if is_negative_cycle:
    print(-1)
else:
    for i in range(1, n):
        print(dist[i])
