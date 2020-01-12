from sys import stdin


def bfs(init_v):
    queue = list()
    visited[init_v] = True
    queue.append(init_v)

    dist[init_v] = 0
    amount_of_friends = 0

    # dist[v]가 2일 때, v와 인접하면서 아직 방문하지 않은 정점들은 init_v 와의 거리가 3이 될 것이므로 친구의 친구라는 조건을 만족하지 않음.
    # 친구, 친구의 친구에 해당하는 정점들은 이미 방문을 마쳤으므로 amount_of_friends 를 리턴한다.
    while queue:
        v = queue.pop(0)
        if dist[v] == 2:
            return amount_of_friends

        for adj_v in adjacent_list[v]:
            if not visited[adj_v]:
                visited[adj_v] = True
                queue.append(adj_v)
                dist[adj_v] = dist[v] + 1
                amount_of_friends += 1

    return amount_of_friends


n = int(stdin.readline().strip('\n'))
m = int(stdin.readline().strip('\n'))

adjacent_list = [list() for _ in range(n)]
for _ in range(m):
    v1, v2 = list(map(int, stdin.readline().split()))
    adjacent_list[v1-1].append(v2-1)
    adjacent_list[v2-1].append(v1-1)

visited = [False for _ in range(n)]
dist = [-1 for _ in range(n)]

print(bfs(0))
