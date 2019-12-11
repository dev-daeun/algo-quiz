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
        '''
        스도쿠 판이 모두 채워졌을 경우 판을 모두 출력한 후 프로세스를 종료한다.
        프로세스 종료가 아닌 리턴을 할 경우 판이 모두 채워진 뒤에 아직 종료되지 않은 재귀가 실행됨.
        '''
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
            '''
            재귀호출을 한 뒤에 cell을 다시 0으로 갱신한다.
            cells는 스택에 쌓인 모든 함수들이 참조하는 전역변수이므로 
            어떤 재귀함수에 의해 변경된 cell의 값이 다른 재귀함수에서 숫자를 채우기 위한 조건을 검사하는 데 영향을 준다.
            '''
            cells[x][y] = 0


answer(0)
