"""
특이한 점은 직선도로는 100원, 코너는 500원으로 비용이 존재한다는것
같은 값을 가진 방법이 여러개가 있을 수 있고, 거기서 또 다음에 어느 방향으로 가느냐에 따라 이전값중에 어느위치가 더 유리한지가 달라짐
나는 해당 위치에서 바로 직전 방향만 생각하면된다고 생각했는데 수차례를 거치면서 유리했다 안유리했다 해지는 예외케이스가 존재하더라 ^^...
=> 3차원 배열로 dp를 관리. 각 좌표마다 상하좌우 최소값을 보관해두는 방식
"""

import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

cost_dir = []
que = deque()

dx = [0, 1, 0, -1]  # right=0 down=1 left=2 up=3
dy = [1, 0, -1, 0]


def init(n):
    global cost_dir, que
    cost_dir = [[[INF]*4 for _ in range(n)] for _ in range(n)]

    # nx, ny, direction, newCost
    que.append((0, 0, 0, 0))
    que.append((0, 0, 1, 0))
    for i in range(4):
        cost_dir[0][0][i] = 0


def solution(board):
    global cost_dir, que
    n = len(board)
    init(n)

    while que:
        cx, cy, d, cost = que.popleft()

        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
                new_cost = cost + (100 if d == i else 600)

                if cost_dir[nx][ny][i] > new_cost:
                    cost_dir[nx][ny][i] = new_cost
                    que.append((nx, ny, i, new_cost))

    return min(cost_dir[n-1][n-1])


board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
print(solution(board))
