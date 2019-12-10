from sys import stdin

cells = list()
for _ in range(9):
    cells.append(list(map(int, stdin.readline().strip('\n').split())))


empty_cells = list()
for i in range(9):
     for j in range(9):
        if cells[i][j] == 0:
            empty_cells.append((i, j))


def garo(x, y):
    return [cells[x][j] for j in range(9)]


def sero(x, y):
    return [cells[i][y] for i in range(9)]


def sagak(x, y):
    result = list()
    for i in range(3 *(x//3), 3*(x//3) + 3):
        for j in range(3*(y//3), 3*(y//3) + 3):
            if i != x or j != y:
                result.append(cells[i][j])
    return result


def answer(idx, result):
    if len(result) == len(empty_cells):
        for r, corp in zip(result, empty_cells):
            r = int(r)
            x, y = corp
            cells[x][y] = r
        return

    x, y = empty_cells[idx]
    for i in range(1, 10):
        if (i not in garo(x, y)) and (i not in sero(x, y)) and (i not in sagak(x, y)):
            cells[x][y] = i
            answer(idx + 1, result + str(i))

answer(0, '')
for row in cells:
    print(' '.join(str(e) for e in row))

