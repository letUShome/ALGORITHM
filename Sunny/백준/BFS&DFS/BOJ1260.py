import sys
from collections import deque

def bfs(list, n, m, v):
    visited = [0 for _ in range(n+1)]
    q = deque()
    q.append(v)
    while q:
        current = q.popleft()
        if visited[current] == 0:
            visited[current] = 1
            print(current, end=" ")
            if current in list:
                for next in list[current]:
                    if visited[next] == 0:
                        q.append(next)
def dfs(list, n, m, v, visited):
    visited[v] = 1
    print(v, end=" ")

    if v in list:
        next = list[v]
        for i in next:
            if visited[i] == 0 and i in list[v]:
                dfs(list, n, m, i, visited)

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    list = {}
    for i in range(m):
        x, y = map(int, input().split())
        if x not in list:
            list[x] = [y]
        else:
            list[x].append(y)
        if y not in list:
            list[y] = [x]
        else:
            list[y].append(x)

    for x in list:
        list[x].sort()
    # print(list)
    visited = [0 for _ in range(n + 1)]
    dfs(list, n, m, v, visited)
    print()
    bfs(list, n, m, v)