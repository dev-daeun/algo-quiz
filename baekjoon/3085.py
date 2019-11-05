from collections import Counter
from sys import stdin


table = []

N = int(stdin.readline())
for _ in range(N):
    row = list(stdin.readline())
    table.append(row)

answer = 0

# 가로 교환
for i in range(N):
    for j in range(N):
        if 0 <= j <= N-2:
            table[i][j], table[i][j+1] = table[i][j+1], table[i][j]

        for row in table:
            c = Counter(row)
            answer = max(answer, c['Y'], c['P'], c['C'], c['Z'])

        for l in range(N):
            column = []

            for r in range(N):
                column.append(table[r][l])

            c = Counter(column)
            answer = max(answer, c['Y'], c['P'], c['C'], c['Z'])

# 세로 교환
for i in range(N):
    for j in range(N):
        if 0 <= i <= N-2:
            table[i][j], table[i+1][j] = table[i+1][j], table[i][j]

        for row in table:
            c = Counter(row)
            answer = max(answer, c['Y'], c['P'], c['C'], c['Z'])

        for l in range(N):
            column = []

            for r in range(N):
                column.append(table[r][l])

            c = Counter(column)
            answer = max(answer, c['Y'], c['P'], c['C'], c['Z'])


print(answer)
