from sys import stdin


# (x, y) 칸에서 이동 가능한(인접한) 경로 리스트
def get_adjacent_cells(x, y):
    return (
        (x - 2, y - 1),
        (x - 2, y + 1),
        (x - 1, y - 2),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x + 1, y + 2),
        (x + 2, y - 1),
        (x + 2, y + 1),
    )


# 몇 번만에 목적지에 도착하는가? => 정점을 방문할 때마다 출발점 ~ 정점 사이의 거리를 저장.
def bfs(start_x, start_y, end_x, end_y, distance, visited, I):
    queue = list()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True

    while queue:
        x, y = queue.pop(0)
        for adj_x, adj_y in get_adjacent_cells(x, y):
            if 0 <= adj_x < I and 0 <= adj_y < I:

                if adj_x == end_x and adj_y == end_y:
                    return distance[x][y] + 1

                if not visited[adj_x][adj_y]:
                    visited[adj_x][adj_y] = True
                    distance[adj_x][adj_y] = distance[x][y] + 1
                    queue.append((adj_x, adj_y))


num_of_tests = int(stdin.readline().strip('\n'))
answers = list()
for _ in range(num_of_tests):
    I = int(stdin.readline().strip('\n'))
    
    distance = list()
    visited = list()
    for _ in range(I):
        distance.append([0 for _ in range(I)])
        visited.append([False for _ in range(I)])

    start_x, start_y = list(map(int, stdin.readline().split()))
    end_x, end_y = list(map(int, stdin.readline().split()))

    if start_x == end_x and start_y == end_y:
        answers.append(0)
        continue

    result = bfs(start_x, start_y, end_x, end_y, distance, visited, I)
    answers.append(result)


for ans in answers:
    print(ans)
