import sys
from collections import deque
import math
'''
최소 거리 그래프 = 다익스트라로 풀이
'''
def solution(n, array):
    distance = [[math.inf for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dxdy = [[0, 1], [0, -1], [-1, 0], [1, 0]]

    q = deque()
    q.append([0, 0])
    distance[0][0] = array[0][0]

    while q:
        p = q.popleft()
        x = p[0]
        y = p[1]
        visited[0][0] = 1

        for np in dxdy:
            nx = x + np[0]
            ny = y + np[1]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if distance[nx][ny] > distance[x][y] + array[nx][ny]:
                        distance[nx][ny] = distance[x][y] + array[nx][ny]
                        q.append([nx, ny])
    return distance[n-1][n-1]

if __name__ == '__main__':
    i = 1;
    n = 9 * 125;
    while n != 0:
        n = int(input());
        if n == 0:
            break;
        array = [list(map(int, input().split())) for _ in range(n)]
        print("Problem " + str(i) + ": " + str(solution(n, array)))
        i += 1
