from sys import stdin

V = int(stdin.readline())

adjacent_list = list()
for _ in range(V):
    adjacent_list.append(list())

for _ in range(V):
    v, *info, eol = list(map(int, stdin.readline().strip('\n').split()))
    for i in range(0, len(info) - 1, 2):
        u, dist = info[i], info[i+1]
        adjacent_list[v-1].append((u - 1, dist))
        adjacent_list[u-1].append((v - 1, dist))


'''
* 트리의 지름 구하는 과정 *

1. 임의의 정점 s에서 가장 거리가 먼 정점 v1을 찾는다. 
2. v1에서 가장 거리가 먼 정점 v2를 찾는다.
3. v1과 v2의 거리가 트리의 지름이다.

BFS를 이용하여 어떤 정점과 인접한 것을 탐색할 때마다 s로부터의 거리를 distances 배열에 저장한다.
distances 배열에서 가장 큰 값에 해당하는 index가 가장 먼 정점이다.   

'''
def find_farthest_vertex(init_v):
    distances = [0 for _ in range(V)]
    visited = [False for _ in range(V)]

    queue = list()
    queue.append(init_v)
    visited[init_v] = True

    while queue:
        v = queue.pop(0)
        for next_v, dist in adjacent_list[v]:
            if not visited[next_v]:
                visited[next_v] = True
                distances[next_v] = distances[v] + dist
                queue.append(next_v)

    return distances.index(max(distances))


def find_distance_between_two(v1, v2):
    visited = [False for _ in range(V)]
    distances = [0 for _ in range(V)]

    queue = list()
    queue.append(v1)
    visited[v1] = True

    while queue:
        v = queue.pop(0)
        for next_v, dist in adjacent_list[v]:
            if next_v == v2:
                return distances[v] + dist
            if not visited[next_v]:
                visited[next_v] = True
                distances[next_v] = distances[v] + dist
                queue.append(next_v)

    return -1


def get_answer():
    v1 = find_farthest_vertex(0)
    v2 = find_farthest_vertex(v1)

    print(find_distance_between_two(v1, v2))


get_answer()
