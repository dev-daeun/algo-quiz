from sys import stdin


N, K = list(map(int, stdin.readline().split()))
MAX_AMOUNT = 100000 * 2

visited = [False for _ in range(MAX_AMOUNT + 1)]
dist = [0 for _ in range(MAX_AMOUNT + 1)]


def adjacent_list(v):
    return (
        ('2x', v * 2),
        ('+1', v + 1),
        ('-1', v - 1),
    )


'''
** 그래프 내의 간선의 가중치가 0 또는 1인 경우 BFS + Dequeue 으로 해결 가능함 **

어떤 정점을 덱에서 pop()했을 때 

1. 인접한 정점과의 거리가 0인 경우에는 push_front(), 
2. 거리가 1인 경우에는 push_back() 한다.


기존의 BFS에서 큐에 정점이 쌓이는 기준은 시작 정점과의 거리다. 
즉, 시작 정점과 가까울 수록 큐에 먼저 쌓이게 된다. 
이 점을 이용하여 최근에 pop()된 정점과의 거리가 0인 정점은 그냥 덱의 front에 push()하여 다음 순회에서 바로 pop() 될 수 있도록 하는 것.
'''


def bfs_by_dequeue():
    dequeue = list()
    dequeue.append(N)
    visited[N] = True

    while dequeue:
        x = dequeue.pop(0)
        if x == K:
            return dist[x]
        for flag, next_v in adjacent_list(x):
            if 0 <= next_v <= MAX_AMOUNT:
                if not visited[next_v]:
                    visited[next_v] = True
                    if flag == '2x':
                        dist[next_v] = dist[x]
                        dequeue.insert(0, next_v)
                    else:
                        dist[next_v] = dist[x] + 1
                        dequeue.append(next_v)

    return dist[K]


print(bfs_by_dequeue())

