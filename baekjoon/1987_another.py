from sys import stdin


R, C = list(map(int, stdin.readline().split()))

cell = list()
for _ in range(R):
    cell.append(list(stdin.readline().strip('\n')))


visited = [False for _ in range(26)]


def adjacent_list(x, y):
    return (
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
    )


answer = 1

'''
알파벳 별로 방문 여부를 저장함.
어떤 정점이 더 이상 promising 하지 않으면 그 정점에 해당하는 알파벳은 방문하지 않은 상태로 원복함. (다른 유망한 정점에서의 탐색을 위해.)
'''


def get_answer(x, y, cnt):
    global answer
    for next_x, next_y in adjacent_list(x, y):
        if 0 <= next_x < R and 0 <= next_y < C:
            if not visited[ord(cell[next_x][next_y]) - 65]:
                visited[ord(cell[next_x][next_y]) - 65] = True
                result = get_answer(next_x, next_y, cnt + 1)
                if result > answer:
                    answer = result
                visited[ord(cell[next_x][next_y]) - 65] = False
    return cnt


visited[ord(cell[0][0]) - 65] = True
get_answer(0, 0, 1)
print(answer)
