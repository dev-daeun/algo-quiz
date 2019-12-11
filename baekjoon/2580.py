from sys import stdin, exit

cells = list()
for _ in range(9):
    cells.append(list(map(int, stdin.readline().strip('\n').split())))


empty_cells = list()
for i in range(9):
    for j in range(9):
        if cells[i][j] == 0:
            empty_cells.append((i, j))


def garo(x, i):
    for yy in range(9):
        if cells[x][yy] == i:
            return False
    return True


def sero(y, i):
    for xx in range(9):
        if cells[xx][y] == i:
            return False
    return True


def sagak(x, y, i):
    start_x = 3 * (x // 3)
    start_y = 3 * (y // 3)

    for xx in range(start_x, start_x + 3):
        for yy in range(start_y, start_y + 3):
            if cells[xx][yy] == i:
                return False

    return True


def answer(idx):
    if idx == len(empty_cells):
        for i in range(9):
            for j in range(9):
                print(cells[i][j], end=' ')
            print()
        exit(0)

    x, y = empty_cells[idx]
    for i in range(1, 10):
        if garo(x, i) and sero(y, i) and sagak(x, y, i):
            cells[x][y] = i
            answer(idx + 1)
            cells[x][y] = 0


answer(0)
