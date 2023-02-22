'''
1. 딕셔너리: {시작점: [도착점들]} // 여기까지는 나와 같다
2. 도착점들의 리스트를 역순 정렬
    - 알파벳 순서상 빠른 것이 우선시
    - 역순으로 정렬하면 모든 방법을 탐색하지 않고 원하는 답 찾기 가능

# 복습 필요
# 백트래킹 공부해야할듯
'''

from collections import deque
from collections import defaultdict


def solution(tickets):
    answer = []

    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)

    for key in graph.keys():
        graph[key].sort(reverse=True)

    stack = ["ICN"]
    while stack:
        top = stack.pop()
        if top not in graph or not graph[top]:
            answer.append(top)
        else:
            stack.append(top)
            stack.append(graph[top].pop())

    return answer[::-1]