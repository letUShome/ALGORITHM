import sys

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
max_val = max(map(max, board))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]
answer = 0

def dfs(x, y, step, total):
    global answer

    # 더 탐색을 진행하더라도 최대값보다 작을 경우
    if total + max_val * (4-step) <= answer:
        return

    # 블록 4개 완성한 경우
    if step == 4:
        answer = max(answer, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if step == 2:
                visited[nx][ny] = 1
                dfs(x, y, step+1, total+board[nx][ny])
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, step+1, total+board[nx][ny])
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0
print(answer)