import sys
from queue import Queue
input = sys.stdin.readline


def sorting(data, rev):
		for list in data:
        list.sort(reverse=rev)


def dfs(n, v, data):
    visit = [False for _ in range(n + 1)]
    stack = [v]

    while stack:
        now = stack.pop()
        if not visit[now]:
            print(now, end=" ")
            visit[now] = True
        else:
            continue

        for node in data[now]:
            if visit[node] is False:
                stack.append(node)


def bfs(n, v, data):
    visit = [False for _ in range(n+1)]
    queue = Queue()
    queue.put(v)

    while queue:
        now = queue.get()
        if not visit[now]:
            print(now, end=" ")
            visit[now] = True
        else:
            continue

        for node in data[now]:
            if not visit[node]:
                queue.put(node)


def solution(n, v, data):
    sorting(data, True)
    dfs(n, v, data)
    print()
    sorting(data, False)
    bfs(n, v, data)


if __name__ == '__main__':
    n, e, v = map(int, input().split())
    data = [[] for _ in range(n+1)]

    for i in range(e):
        v1, v2 = map(int, input().split())
        data[v1].append(v2)
        data[v2].append(v1)

    solution(n, v, data)