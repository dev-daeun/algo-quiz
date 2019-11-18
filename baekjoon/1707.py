from sys import stdin

S1_VISITED = 0
S2_VISITED = 1
NOT_VISITED = 2

def is_binary_graph(V, i, status, adjacent_list):
    queue = list()
    queue.append(i)
    status[i] = S1_VISITED

    while queue:
        x = queue.pop(0)
        for v in adjacent_list[x]:
            if status[v] == status[x]:
                return False
            if status[v] == NOT_VISITED:
                status[v] = S1_VISITED if status[x] == S2_VISITED else S2_VISITED
                queue.append(v)
    
    return True


def search_whole_graph(V, adjacent_list):
    status = [NOT_VISITED for _ in range(V)]
    for i in range(V):
        if status[i] == NOT_VISITED:
            result = is_binary_graph(V, i, status, adjacent_list)
            if result == False:
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
