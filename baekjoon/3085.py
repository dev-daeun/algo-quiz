from sys import stdin


table = []

N = int(stdin.readline())
for _ in range(N):
    row = list(stdin.readline().strip('\n'))
    table.append(row)

answer = 0
counter = {
    'Y': 0,
    'C': 0,
    'Z': 0,
    'P': 0,
}


def calculate_max(line):
    cur = line[0]
    for candy in line:
        if candy == cur:
            counter[cur] += 1
        else:
            counter[cur] = 0
            counter[candy] += 1
        cur = candy
    global answer
    nomi = [counter[key] for key in counter]
    return max(nomi)


def init_counter():
    for key in counter:
        counter[key] = 0


def create_column(n):
    column = []
    for r in range(N):
        column.append(table[r][n])
    return column


# 가로 교환
for i in range(N):
    for j in range(N):
        if 0 <= j <= N-2:
            table[i][j], table[i][j+1] = table[i][j+1], table[i][j]

            row = table[i]
            a = calculate_max(row)
            init_counter()

            column1 = create_column(j)
            b = calculate_max(column1)
            init_counter()

            column2 = create_column(j+1)
            c = calculate_max(column2)

            answer = max(answer, a, b, c)
            init_counter()

            table[i][j], table[i][j+1] = table[i][j+1], table[i][j]


# 세로 교환
for i in range(N):
    for j in range(N):
        if 0 <= i <= N-2:
            table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

            row1 = table[i]
            a = calculate_max(row1)
            init_counter()

            row2 = table[i+1]
            b = calculate_max(row2)
            init_counter()

            column = create_column(j)
            c = calculate_max(column)
            init_counter()

            answer = max(answer, a, b, c)
            table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

print(answer)
