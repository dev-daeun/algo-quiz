from sys import stdin


N, K = list(map(int, stdin.readline().split()))

MAX_AMOUNT = 100000

'''
방문했던 정점들을 출력하려면 종착점인 K에서부터 역추적이 필요함.
prev[i]: i번째 정점 이전에 방문했던 정점을 기록할 용도.

1. 어떤 정점을 방문할 때마다 그 정점을 기준으로 이전에 방문했던 정점을 기록한다.
2. 스택을 이용하여 K번째 정점부터 N까지의 역순으로 방문했던 정점을 출력한다.
'''
prev = [i for i in range(MAX_AMOUNT + 1)]
visited = [False for _ in range(MAX_AMOUNT + 1)]


def adjacent_list(v):
    return (
        v - 1,
        v + 1,
        v * 2,
    )


def bfs():
    queue = list()
    queue.append(N)
    visited[N] = True

    while queue:
        x = queue.pop(0)
        if x == K:
            return
        for next_v in adjacent_list(x):
            if 0 <= next_v <= MAX_AMOUNT:
                if not visited[next_v]:
                    visited[next_v] = True
                    queue.append(next_v)
                    prev[next_v] = x


def print_answer():
    bfs()

    stack = list()
    stack.append(K)

    x = stack[-1]
    while x != prev[x]:
        stack.append(prev[x])
        x = prev[x]

    print(len(stack) - 1)
    print(' '.join(str(r) for r in reversed(stack)))


print_answer()
