from sys import stdin

S1_VISITED = 0
S2_VISITED = 1
NOT_VISITED = 2

'''
is_binary_graph():
DFS를 사용해서 어떤 정점을 방문하고나서는, 그 정점과 연결된 다른 정점들은 다른 집합에 있다고 간주한다.
어떤 정점과 연결된 다른 정점을 방문했을 때 두 정점이 같은 집합에 있으면 이분 그래프가 아니므로 False 리턴.
아니면 True 리턴.

하나의 정점과 연결된 다른 정점들의 각 방문 여부를 체크해서 리스트에 따로 저장하고 리스트를 검사했을 때 시간 초과가 났음.
항상 각 정점의 인접리스트를 끝까지 순회하였으므로 dfs의 시간복잡도 = 항상 O(전체 간선의 개수)

인접 리스트를 순회하면서 가장 먼저 발견한 미방문 정점을 무조건 스택에 저장 후 for문을 break하도록 변경 후 통과.
'''


# 재귀 없는 dfs 구현
def is_binary_graph(init, status, adjacent_list):
    stack = list()
    stack.append(init)
    status[init] = S1_VISITED

    while stack:
        x = stack[-1]
        is_pushed = False

        for v in adjacent_list[x]:
            if status[v] == status[x]:
                return False

            if status[v] == NOT_VISITED:
                status[v] = S1_VISITED if status[x] == S2_VISITED else S2_VISITED
                stack.append(v)
                is_pushed = True
                break

        if not is_pushed:
            stack.pop(-1)

    return True


'''
이분 그래프:
1. 그래프 내부에 2개의 분리된(두 그래프를 잇는 경로가 전혀 없는) 그래프가 있거나
2. 그래프 내 모든 정점들을 두 집합으로 분류했을 때 같은 집합에 있는 정점들 사이에는 경로가 존재하지 않는 그래프.

search_whole_graph()에서 각 부분 그래프들을 DFS한다.
'''


def search_whole_graph(V, adjacent_list):
    status = [NOT_VISITED for _ in range(V)]
    for i in range(V):
        if status[i] == NOT_VISITED:
            result = is_binary_graph(i, status, adjacent_list)
            if not result:
                return 'NO'
    return 'YES'


num_of_test = int(stdin.readline())
answers = list()
for _ in range(num_of_test):
    V, E = list(map(int, stdin.readline().split()))

    adjacent_list = list()
    for _ in range(V):
        adjacent_list.append(list())

    for _ in range(E):
        v1, v2 = list(map(int, stdin.readline().split()))
        adjacent_list[v1-1].append(v2 - 1)
        adjacent_list[v2-1].append(v1 - 1)

    answers.append(search_whole_graph(V, adjacent_list))

for ans in answers:
    print(ans)
