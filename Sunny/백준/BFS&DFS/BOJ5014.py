'''
백준
실버 1
스타트링크
Sol 2 -> 시간초과
'''

from collections import deque
# 총 F층
# 목표 층은 G층
# 현재 위치 S층
# U = 현재 + U
# D = 현재 - D
# 100 2 1 1 0
# 10 1 10 2 1

def bfs():
    q = deque([start])
    visited[start] = 1
    while q:
        current = q.popleft()
        if current == go:
            return count[go]
        if 0 < current + up <= full and visited[current + up] == 0:
            count[current + up] = count[current] + 1
            visited[current + up] = 1
            q.append(current + up)
        if 0 < current - down <= full and visited[current - down] == 0:
            count[current - down] = count[current] + 1
            q.append(current - down)
            visited[current - down] = 1
    if count[go] == 0:
        return "use the stairs"

full, start, go, up, down = map(int, input().split())
visited = [0 for _ in range(full+1)]
visited[0] = 1
count = [0 for _ in range(full+1)]
print(bfs())
