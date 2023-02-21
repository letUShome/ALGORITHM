from collections import deque
import sys
import copy

'''
빙산의 부분별 높이 정보는 배열의 각 칸에 양수로 저장
빙산 이외 바다에는 0
동서남북 네 방향으로 붙어있는 0이 저장된 칸 개수만큼 줄어듦

빙산이 두 덩어리 이상으로 분리되는 최초의 시간

Solution)
    1. 빙산의 모습을 변화시키는 함수
        1-1. 0이 아닌 숫자가 있는 좌표를 q에 저장
        1-2. 좌표에서 주변에 0이 몇 개 있는지 탐색
    2. 1년이 탐색되면 빙산이 분리되었는지 탐색
        2-1. 기억은 잘 안 나지만... 단지수 세기 했던 코드 잠깐 참고하면 될듯

Solution2)
    현재 bfs로 모든 빙산을 깎게 만들었는데 그렇게하면 한 번 실행밖에 안 됨
    두 번 이상 실행시켜야 함
    혹은 빙산이 분리되었는지 체크하는 코드가 필요한데, 어떻게 짤 수 있을지 감이 안 옴
'''

n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for __ in range(n)]
iceberg_cnt = 1
year = 0;

def count_sea_spots(iceberg, x, y):
    cnt = 0
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if iceberg[nx][ny] == 0:
                cnt += 1
    return cnt

def bfs(i, j):
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    q = deque()
    copy_iceberg = copy.deepcopy(iceberg)
    q.append([i, j])
    copy_iceberg[i][j] -= count_sea_spots(iceberg, i, j)
    while q:
        xy = q.popleft()
        for d in dxy:
            nx = xy[0] + d[0]
            ny = xy[1] + d[1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if iceberg[nx][ny] != 0:
                    copy_iceberg[nx][ny] -= count_sea_spots(iceberg, nx, ny)
                    if copy_iceberg[nx][ny] < 0:
                        copy_iceberg[nx][ny] = 0
                visited[nx][ny] = 1
                q.append([nx, ny])
    return copy_iceberg

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and iceberg[i][j] != 0:
                bfs(i, j)
    year += 1
    if year == 3:
        break


print(year)




'''
while iceberg_cnt == 1:
    result = 0
    
    iceberg = bfs(n, m, iceberg)
    year += 1
'''





