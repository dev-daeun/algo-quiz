from sys import stdin, maxsize


class Vertex:
    def __init__(self, number):
        self.number = number
        self.dist = maxsize


def relax(v, adj_v, w, vertices):
    if vertices[v].dist + w < vertices[adj_v].dist:
        vertices[adj_v].dist = vertices[v].dist + w


def dijkstra(start, adjacent_list, n):
    vertices = [Vertex(i) for i in range(n)]
    vertices[start].dist = 0

    q = list()
    for i in range(n):
        q.append(vertices[i])

    while q:
        q = sorted(q, key=lambda x: x.dist)
        v = q.pop(0)

        for adj_v, adj_w in adjacent_list[v.number]:
            relax(v.number, adj_v, adj_w, vertices)

    return vertices


if __name__ == '__main__':
    n, m = list(map(int, stdin.readline().split()))
    start = int(stdin.readline().strip('\n'))
    start -= 1  # 0-index based

    adjacent_list = [list() for _ in range(n)]
    for _ in range(m):
        v1, v2, w = list(map(int, stdin.readline().split()))
        if len(adjacent_list[v1-1]) > 0:
            for adj in adjacent_list[v1-1]:
                adj_v, adj_w = adj
                if adj_v == v2 - 1 and adj_w > w:
                    adjacent_list[v1-1].pop(adjacent_list[v1-1].index(adj))

        adjacent_list[v1-1].append((v2 - 1, w))

    vertices = dijkstra(start, adjacent_list, n)

    for v in vertices:
        print('INF') if v.dist == maxsize else print(v.dist)
