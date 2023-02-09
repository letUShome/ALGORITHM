import sys
from collections import deque;
'''
수빈 = 점 N => 걷거나 순간이동 가능(위치가 X일 때)
    - 걸을 때: 1초 후에 X-1 || X+1
    - 순간이동: 1초 후에 2*X의 위치로 이동
동생 = 점 K

=> 수빈이가 동생을 찾을 수 있는 가장 빠른 시간

Solution)
위치 X에 대해
    1. X-1로 갔을 때
    2. X+1로 갔을 때
    3. 2*X로 갔을 때
=> 그래프를 그리며 BFS로 탐색한다.
'''

def solution(n, k):
    MAX = 10 ** 5; # 점의 최대 크기는 100000
    array = [0] * (MAX+1); # array의 각 인덱스에는 걸린 시간을 저장한다.

    q = deque();
    q.append(n);

    while q:
        x = q.popleft(); # queue의 첫번째 요소부터 시작
        if x == k: # 현재 x의 위치가 k와 같다면 return
            return array[x];
        for nx in (x-1, x+1, x*2): # 세 요소 중에서
            if 0 <= nx <= MAX and not array[nx]: # array[nx]가 0일 때 (not false => true)
                array[nx] = array[x] + 1;
                q.append(nx);
    return 0;


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solution(N, K));