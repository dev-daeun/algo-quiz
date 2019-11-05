from sys import stdin

# 모든 칸들을 순회하면서 교환 결과를 비교한다.
# 교환 결과: 무조건 1번의 교환이 발생해야 하므로, 교환이 발생하고 난 뒤에 변경되는 행과 열로부터 구한 최대 사탕 갯수.
# calculate_max()에서 최대 사탕 갯수를 구하는 로직에 오류가 있어서 시간 다소 소요.

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
    counts = [1]
    for i in range(1, N):
        candy = line[i]
        if cur == candy:
            counts[-1] += 1
        else:
            counts.append(1)
        cur = candy
    return max(counts)

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

            # 딱 1번의 교환만 가정하므로 원복시킨다.
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

            # 딱 1번의 교환만 가정하므로 원복시킨다.
            table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

print(answer)
