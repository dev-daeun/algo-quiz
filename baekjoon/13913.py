from copy import deepcopy
from sys import stdin


# path: N부터 정점 V까지 이동하는 경로.
# path 의 길이 = 이동하는 데 걸린 시간(초 단위)
class Vertex:
    def __init__(self, val):
        self.val = val
        self.path = []


N, K = list(map(int, stdin.readline().split()))

MAX_AMOUNT = 100000
vertexes = list()
for i in range(MAX_AMOUNT+1):
    vertexes.append(Vertex(i))


def adjacent_list(v):
    return (
        v - 1,
        v + 1,
        v * 2,
    )


def bfs():
    queue = list()
    queue.append(N)
    vertexes[N].path.append(N)

    while queue:
        x = queue.pop(0)
        for next_v in adjacent_list(x):
            if 0 <= next_v <= MAX_AMOUNT:
                if not vertexes[next_v].path or len(vertexes[x].path) + 1 < len(vertexes[next_v].path):
                    vertexes[next_v].path = deepcopy(vertexes[x].path)
                    vertexes[next_v].path.append(next_v)
                    queue.append(next_v)
                if next_v == K:
                    return vertexes[next_v].path

    return vertexes[K].path


def get_answer():
    result = bfs()
    print(len(result) - 1)
    print(' '.join([str(r) for r in result]))


get_answer()
