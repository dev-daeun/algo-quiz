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
    nomi.append(answer)
    answer = max(nomi)


# 가로 교환
for i in range(N):
    for j in range(N):
        if 0 <= j <= N-2:
            if table[i][j] != table[i][j+1]:
                table[i][j], table[i][j+1] = table[i][j+1], table[i][j]

                for row in table:
                    calculate_max(row)

                for l in range(N):
                    column = []
                    for r in range(N):
                        column.append(table[r][l])
                    calculate_max(column)

                table[i][j], table[i][j+1] = table[i][j+1], table[i][j]

# 세로 교환
for i in range(N):
    for j in range(N):
        if 0 <= i <= N-2:
            if table[i][j] != table[i+1][j]:
                table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

                for row in table:
                    calculate_max(row)

                for l in range(N):
                    column = []
                    for r in range(N):
                        column.append(table[r][l])
                    calculate_max(column)

                table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

print(answer)
