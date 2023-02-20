import sys
from collections import deque

'''
1 = 이동 가능
0 = 이동 불가능
(1, 1) -> (n, m) 지나야 하는 최소 칸 수 구하기
'''
def bfs(n, m, maze):
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()
    q.append([0, 0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = [[0 for _ in range(m)] for _ in range(n)]
    visited[0][0] = 1
    cnt[0][0] = 1
    while q:
        xy = q.popleft()
        for d in dxdy:
            nx = xy[0] + d[0]
            ny = xy[1] + d[1]
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt[nx][ny] = cnt[xy[0]][xy[1]] + 1
                q.append([nx, ny])
    return cnt[n-1][m-1]

if __name__ == '__main__':
    n, m = map(int, input().split(sep=" "))
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input())))
    print(bfs(n, m, maze))