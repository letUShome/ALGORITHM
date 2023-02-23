'''
백준
실버 1
스타트링크
'''

from collections import deque
# 총 F층
# 목표 층은 G층
# 현재 위치 S층
# U = 현재 + U
# D = 현재 - D
# dfs로 풀면 될듯

def dfs(current, cnt):
    # print(current, cnt, go, down)
    visited[current] = 1
    if current == go:
        result.append(cnt)
        return
    if 0 not in visited:
        return
    if current + up <= full and visited[current + up] == 0:
        visited[current + up] = 1
        dfs(current+up, cnt+1)
    if current - down > 0 and visited[current - down] == 0:
        visited[current - down] == 1
        dfs(current-down, cnt+1)

# 100 2 1 1 0
# 10 1 10 2 1
full, start, go, up, down = map(int, input().split())

visited = [0 for _ in range(full+1)]
visited[0] = 1
result = []
dfs(start, 0)
result.sort()

if len(result) == 0:
    print("use the stairs")
else:
    print(result)
    print(result[0])
