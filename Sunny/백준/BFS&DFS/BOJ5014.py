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
# dfs로 풀면 될듯

def bfs():
    q = deque()
    q.append((start, 0))
    while q:
        current = q.popleft()
        visited[current[0]] = 1
        if current[0] == go:
            result.append(current[1])
            break
        if 0 not in visited:
            break
        if current[0] + up <= full and visited[current[0] + up] == 0:
            q.append((current[0] + up, current[1] + 1))
        if current[0] - down > 0 and visited[current[0] - down] == 0:
            q.append((current[0] - down, current[1] + 1))

# 100 2 1 1 0
# 10 1 10 2 1
full, start, go, up, down = map(int, input().split())

visited = [0 for _ in range(full+1)]
visited[0] = 1
result = []
bfs()
result.sort()

if len(result) == 0:
    print("use the stairs")
else:
    # print(result)
    print(result[0])
