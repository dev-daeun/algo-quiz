from sys import stdin


R, C = list(map(int, stdin.readline().split()))

cell = list()
for _ in range(R):
    cell.append(list(stdin.readline().strip('\n')))

'''
푸는 데 걸린 시간: 3시간

* 푸는 데 시간이 오래 걸린 원인 *
    1. max() 내장함수에 재귀호출되는 함수를 넘겨줘서 의도한대로 동작하지 않음.

* 시간 초과 원인 *
    1. visited 컬렉션을 (알파벳 문자: False) 형태의 해시테이블로 만들었음.
    2. (ASCII 코드 - 65) 인덱스로 접근하는 리스트로 바꾼 후 통과됨.
'''
visited = [False for _ in range(26)]


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
            if not visited[ord(cell[next_x][next_y]) - 65]:
                visited[ord(cell[next_x][next_y]) - 65] = True
                # 재귀호출하는 함수를 넣어서 그런지
                # max(answer, get_answer(next_x, next_y, cnt + 1)) 으로 호출하면 의도하는 값이 안나옴.
                result = get_answer(next_x, next_y, cnt + 1)
                if result > answer:
                    answer = result
                visited[ord(cell[next_x][next_y]) - 65] = False
    return cnt


visited[ord(cell[0][0]) - 65] = True
get_answer(0, 0, 1)
print(answer)
