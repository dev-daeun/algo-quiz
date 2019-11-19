from sys import stdin

'''
(i, j) 칸에서 걸어갈 수 있는 경로
-------------------------------
  i-1, j-1 | i-1, j | i-1, j+1 
-------------------------------
  i,   j-1 | i,   j | i,   j+1  
-------------------------------
  i+1, j-1 | i+1, j | i+1, j+1
-------------------------------

(i, j)의 adjacent vertexes = 주변 8개 칸들

1. 전체 각 칸을 순회하면서 칸이 땅인 경우(1인 경우) 칸과의 경로가 있는 모든 cell 탐색(부분 그래프 탐색).
2. 탐색이 끝나면 cnt += 1 

* 2차원 배열이 입력으로 주어지므로 인접행렬 사용.
'''
X_MOVE = [-1, 0, 1]
Y_MOVE = [-1, 0, 1]
def dfs(init_x, init_y, map_, visited, W, H):
    stack = list()
    stack.append((init_x, init_y))
    visited[init_x][init_y] = True

    while stack:
        x, y = stack[-1]
        is_pushed = False
        for m in X_MOVE:
            for n in Y_MOVE:
                adjacent_x = x + m
                adjacent_y = y + n
                if 0 <= adjacent_x < W and 0 <= adjacent_y < H:
                    if map_[adjacent_x][adjacent_y] == '1' and not visited[adjacent_x][adjacent_y]:
                        visited[adjacent_x][adjacent_y] = True
                        stack.append((adjacent_x, adjacent_y))
                        is_pushed = True
                        break

            if is_pushed:
                break

        if not is_pushed:
            stack.pop(-1)


answers = list()
while True:
    H, W = list(map(int, stdin.readline().strip('\n').split()))
    if not (W or H):
        break

    map_ = list()
    for _ in range(W):
        row = stdin.readline().strip('\n').split()
        map_.append(row)

    visited = list()
    for _ in range(W):
        visited.append([False for _ in range(H)])
        
    cnt = 0
    for i in range(W):
        for j in range(H):
            if map_[i][j] == '1' and not visited[i][j]:
                    dfs(i, j, map_, visited, W, H)
                    cnt += 1
    answers.append(cnt)

for ans in answers:
    print(ans)
