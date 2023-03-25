'''
사람의 수 n
파티의 수 m
'''

import sys

def find(f):
    # 부모가 자기 자신인 경우
    if people[f] < 0:
        return f

    people[f] = find(people[f])
    return people[f]

def union(f1, f2):
    p1 = find(f1)
    p2 = find(f2)

    if p1 == p2:
        return

    if people[p1] < people[p2]:
        people[p1] += people[p2]
        people[p2] = p1
    else:
        people[p2] += people[p1]
        people[p1] = p2
    return

def count_party(party):
    cnt = 0

    # 파티를 한 개씩 순회
    for i in party:
        # 0번 노드의 parent(진실을 아는 사람과 연결됨) & 참석자의 parent
        # 거짓말쟁이로 알려지지 않은 경우므로 두 find의 결과값이 달라야 함
        # 서로 부모가 다른 경우 + 1
        if find(i) != find(0):
            cnt += 1
    return cnt


if __name__ == '__main__':
    # 사람의 수 n, 파티의 수 m
    n, m = map(int, input().split())
    people = [-1 for _ in range(n + 1)]
    party = []

    # [0]진실의 아는 사람의 수 [1:] 수 만큼 사람의 번호
    for truth in map(int, input().split()[1:]):
        # 진실을 아는 사람들을 0번 node 기준으로 union
        union(truth, 0)

    # m개의 파티 참석
    for _ in range(m):
        # [0] 파티 참석자 수 [1:] 참석자의 번호
        arr = list(map(int, input().split()))
        # 파티에 오는 첫번째 사람 저장
        party.append(arr[1])
        # 2번 노드부터 온 사람의 숫자만큼
        for i in range(2, arr[0] + 1):
            union(arr[i], arr[1])

    print(count_party(party))