from sys import stdin

N = int(stdin.readline())

# 어떤 그래프가 트리일 경우, 그래프의 간선의 갯수 = 정점의 갯수 - 1
adjacent_list = list()
for _ in range(N):
    adjacent_list.append(list())

for _ in range(N-1):
    v1, v2 = list(map(int, stdin.readline().split()))
    adjacent_list[v1-1].append(v2 - 1)
    adjacent_list[v2-1].append(v1 - 1)

'''
모든 간선을 입력받더라도 두 정점 중 어느 게 부모이고 자식인지 구분할 수 없음.
1번 노드를 시작정점으로 하여 어떤 정점 v와 인접한 정점들의 부모 노드를 v로 설정한다.
어떤 정점 v와 인접한 정점들을 순회할 때 이미 방문한 정점은 v의 부모이므로 건너뛰어야 한다.
'''
def bfs(init_v):
    visited = [False for _ in range(N)]
    queue = list()
    queue.append(init_v)
    visited[init_v] = True

    parents = [-1 for _ in range(N)]
    while queue:
        v = queue.pop(0)
        for node in adjacent_list[v]:
            if not visited[node]:
                visited[node] = True
                parents[node] = v
                queue.append(node)
    
    return parents


def get_answer():
    result = bfs(0)
    for i in range(1, N):
        print(result[i] + 1)


get_answer()
