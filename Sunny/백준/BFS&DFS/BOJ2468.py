'''
백준
실버 1
안전 영역
'''

'''
주어진 영역 n * n에 대해서
안전 영역의 기준 k가 있을 때
안전 영역의 최대 개수
'''

from collections import deque

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(x, y, k):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        xy = q.popleft()
        for d in dxy:
            nx = xy[0] + d[0]
            ny = xy[1] + d[1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > k and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = 1

# 입출력
n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
count = [0 for _ in range(100+1)]
for k in range(0, 100):
    visited = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and visited[i][j] == 0:
                bfs(i, j, k)
                count[k] += 1
print(max(count))
