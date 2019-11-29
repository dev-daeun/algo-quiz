from sys import stdin

S = int(stdin.readline().strip('\n'))
MAX_AMOUNT = S * 2


'''
현재 화면에 s개의 이모티콘이 있을 때 클립보드에는 몇개가 있는지 알 수 없으므로 클립보드의 모든 경우의 수를 2차원 배열에 기록하고 시작한다.

정점 = 클립보드 & 스크린의 상태

clipboard, screen

(0, 0), (0, 1), (0, 2) ... (0, S)
(1, 0), (1, 1), (1, 2) ... (1, S)
(2, 0), (2, 1), (2, 2) ... (2, S)
...


현재 화면에 s개의 이모티콘이 있고, 클립보드에 c개의 이모티콘이 복사되어 있을 때 1초 후에 가능한 상태, 즉 인접한 정점은 아래와 같다.

(c, c)      # COPY
(c, s + c)  # PASTE
(c, s - 1)  # DELETE


인접한 정점을 탐색하면서 정점에 방문하는 데 걸린 시간, 즉 거리를 dist 배열에 기록한다.
이미 방문한 정점은 이미 최소의 거리를 가지고 있다. => 한번 방문한 정점은 재방문하지 않는다.
'''
status = [list() for _ in range(MAX_AMOUNT + 1)]
for i in range(MAX_AMOUNT + 1):
    for j in range(MAX_AMOUNT + 1):
        status[i].append((i, j))

visited = list()
dist = list()
for _ in range(MAX_AMOUNT + 1):
    visited.append([False for _ in range(MAX_AMOUNT + 1)])
    dist.append([0 for _ in range(MAX_AMOUNT + 1)])


def adjacent_list(c, s):
    # clip, screen
    return (
        (c, c),      # COPY
        (c, s + c),  # PASTE
        (c, s - 1),  # DELETE
    )


def bfs():
    init_clip = 0
    init_s = 1

    queue = list()
    queue.append((init_clip, init_s))
    visited[init_clip][init_s] = True

    while queue:
        clip, screen = queue.pop(0)
        if screen == S:
            return dist[clip][screen]

        for next_c, next_s in adjacent_list(clip, screen):
            if 0 <= next_s <= MAX_AMOUNT:
                if not visited[next_c][next_s]:
                    visited[next_c][next_s] = True
                    dist[next_c][next_s] = dist[clip][screen] + 1
                    queue.append((next_c, next_s))

    return dist[S]


print(bfs())
