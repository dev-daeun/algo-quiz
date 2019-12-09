from sys import stdin


R, C = list(map(int, stdin.readline().split()))

cell = list()
for _ in range(R):
    cell.append(list(stdin.readline().strip('\n')))

'''
푸는 데 걸린 시간: 3시간.........

* 푸는 데 시간이 오래 걸린 원인 *
    재귀함수 안에서 아래와 같은 형태로 max()를 쓰면 max()가 의도한대로 동작하지 않음.

    def get_answer(...):
        ...
        answer = max(answer, get_answer(...))


* 시간 초과 원인 *
    1. visited_alphabets 컬렉션을 (알파벳 문자: False) 형태의 해시테이블로 만들었음.
    2. (ASCII 코드 - 65) 인덱스로 접근하는 리스트로 바꾼 후 통과됨.

* 배운 것 *
    1. 재귀호출한 결과를 어떤 값과 비교하여 최소/최대값을 구할 때 max(), min()은 쓰지말자.
    2. 컬렉션은 왠만하면 리스트(1차원 배열)로 구현하자.
'''


def adjacent_list(x, y):
    return (
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
    )


answer = 1


def get_answer(x, y, visited_alphabets):
    global answer
    for next_x, next_y in adjacent_list(x, y):
        if 0 <= next_x < R and 0 <= next_y < C:
            if cell[next_x][next_y] not in visited_alphabets:
                result = get_answer(next_x, next_y, visited_alphabets + cell[next_x][next_y])
                if result > answer:
                    answer = result
    return len(visited_alphabets)


get_answer(0, 0, visited_alphabets=cell[0][0])
print(answer)
