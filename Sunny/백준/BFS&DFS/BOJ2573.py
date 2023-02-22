'''
거의 다 풀었는데
반례 찾음 -> 아침에 일어나서 마저 하기
3 3
0 0 0
0 0 0
0 0 0

4 4
0 0 0 0
0 1 1 0
0 1 1 0
0 0 0 0

'''

from collections import deque

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]
year = 1
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def count_ocean_spots(x, y):
    cnt = 0
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] == 0:
            cnt += 1
    return cnt

def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for d in dxy:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m and iceberg[nx][ny] != 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

while True:
    visited = [[0 for _ in range(m)] for __ in range(n)]
    count = []
    result = 1
    piece = 0

    flag = False
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                flag = True
            if flag:
                break
    if not flag:
        print(0)
        break

    # 빙산 업데이트
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] != 0:
                count.append([i, j, count_ocean_spots(i, j)])

    for cnt in count:
        iceberg[cnt[0]][cnt[1]] -= cnt[2]
        if iceberg[cnt[0]][cnt[1]] < 0:
            iceberg[cnt[0]][cnt[1]] = 0

    # 빙산 덩어리 개수 세기
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and iceberg[i][j] != 0:
                bfs(i, j)
                piece += 1
    if piece >= 2:
        print(year)
        break

    year += 1