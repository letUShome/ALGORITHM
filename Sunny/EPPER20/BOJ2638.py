import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def bfs():
    q = deque()
    visited = [[0] * m for _ in range(n)]
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if cheese[nx][ny] == 0 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                elif cheese[nx][ny] == 1:
                    visited[nx][ny] += 1

    melted = []
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                melted.append((i, j))

    return melted

while True:
    melted = bfs()
    if not melted:
        break
    answer += 1
    for x, y in melted:
        cheese[x][y] = 0

print(answer)