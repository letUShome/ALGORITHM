from collections import deque

# bfs로 풀이
# maps에서 0은 벽, 1은 통행로

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    # 방문 여부
    visited = [[False for i in range(m)] for j in range(n)]
    return bfs(maps, visited, 0, 0);


def bfs(maps, visited, x, y):
    # n, m 크기
    n = len(maps)
    m = len(maps[0])
    
    # 배열에 (x, y) 쌍을 넣어 선언
    q = deque([(x, y)])
    
    # 방문 체크
    visited[x][y] = True
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    distance = {(x, y) : 0}
    print(distance)
    
    while q:
        x, y = q.popleft() # 왼쪽 첫번째 요소 pop
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= 0 and nx < n and ny >= 0 and ny < m and (visited[nx][ny] == False) and (maps[nx][ny] == 1):
                if nx == n - 1 and ny == m - 1:
                    print(x, y)
                    print(distance[(x, y)] + 2) # (0, 0), (n, m) 두 개의 칸을 더함
                    return distance[(x, y)] + 2
                q.append((nx, ny))
                distance[(nx, ny)] = distance[(x, y)] + 1
                visited[nx][ny] = True
    
    return -1
