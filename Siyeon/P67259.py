"""
그리드 문제 - 0이 벽을 의미함
특이한 점은 직선도로는 100원, 코너는 500원
코너 발생 조건 - 이전 방향하고 다른방향으로 이동했을때
문제는 dp로 풀어야할듯 싶다. 대신 매 칸에 저장해야하는 값은 거리가 아니라 비용
같은 값을 가진 방법이 여러개가 있을 수 있고, 거기서 또 다음에 어느 방향으로 가느냐에 따라 이전값중에 어느위치가 더 유리한지가 달라짐
"""

import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
n = len(board)
dp_cost = [[INF for _ in range(n)] for _ in range(n)]
dp_dir = [[[] for _ in range(n)] for _ in range(n)]
dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열


def solution():
    que = deque()
    que.append((0, 0, 4))
    dp_cost[0][0] = 0

    while que:
        x, y, last_command = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i],
            last_cost = dp_cost[x][y]
            cost = 0

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                if last_command == 4:
                    cost = 100
                elif last_command != i:
                    cost = last_cost + 600
                else:
                    cost = last_cost + 100

                if cost < dp_cost[nx][ny]:
                    dp_cost[nx][ny] = cost
                    dp_dir[nx][ny].append(i)
                    que.append((nx, ny, i))

    return dp_cost[n - 1][n - 1]

print(solution())