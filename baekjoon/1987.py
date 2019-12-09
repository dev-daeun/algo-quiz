from sys import stdin, setrecursionlimit

setrecursionlimit(30000)

R, C = list(map(int, stdin.readline().split()))

cell = list()
visited = list()
for _ in range(R):
    cell.append(list(stdin.readline().strip('\n')))
    visited.append([False for _ in range(R)])


class Alphabets:
    def __init__(self, chars, additional=None):
        self.chars = chars
        if additional:
            self.chars += additional


def is_promising(x, y, visited_alphabets):
    return cell[x][y] not in visited_alphabets.chars


def adjacent_list(x, y):
    return (
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y),
    )


answer = 0


def get_answer(x, y, visited_alphabets):
    global answer
    if 0 <= x < R and 0 <= y < C:
        if is_promising(x, y, visited_alphabets):
            for next_x, next_y in adjacent_list(x, y):
                print(f'x: {next_x}, y:{next_y} ', id(visited_alphabets.chars))
                answer = max(answer, get_answer(next_x, next_y, Alphabets(visited_alphabets.chars, additional=cell[x][y])))

    return len(visited_alphabets.chars)


get_answer(0, 0, Alphabets(''))
print(answer)
