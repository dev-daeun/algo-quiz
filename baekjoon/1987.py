from sys import stdin, setrecursionlimit

setrecursionlimit(30000)

R, C = list(map(int, stdin.readline().split()))

cell = list()
for _ in range(R):
    cell.append(list(stdin.readline().strip('\n')))


alphabets = [chr(i) for i in range(65, 91)]
visited = {alpha: False for alpha in alphabets}


def adjacent_list(x, y):
    return (
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
    )


answer = 1


def get_answer(x, y, cnt):
    global answer
    for next_x, next_y in adjacent_list(x, y):
        if 0 <= next_x < R and 0 <= next_y < C:
            if not visited[cell[next_x][next_y]]:
                visited[cell[next_x][next_y]] = True
                answer = max(answer, get_answer(next_x, next_y, cnt + 1))
                visited[cell[next_x][next_y]] = False

    return cnt


get_answer(0, 0, 1)
print(answer)
