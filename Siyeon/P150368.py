"""
목표: 플러스 가입자 수 증가 > 판매액을 최대로
구입: 특정 할인율 이상일때 -> 총합이 특정이상이면 플러스 가입

1. 일단 원하는 할인율 이상으로 할인하여 다 담게 하고, 그로인해 제한을 넘게 만드는게 목표
2. 1번을 충족하기 위해서는 가장 높은 할인율을 원하는 유저에 맞춰서 할인해봐야할듯
3. 거기서 할인율이 더 낮으면서 한계치를 못넘은 사람들을 유인하기 위해 그들에 맞춰서 할인율을 한두개 내려보기
4. 3번에서 버는돈을 최대화하기 위해 원하는 할인율에 딱 맞춰서 내려보자 (할인율은 40, 30, 20, 10으로 존재함)
-> 여기서 사용할 수 있는 알고리즘은?

입출력2 생각해보기 (1.할인율 2.한계치 순으로 정렬해보자- 다 딱 떨어지게 바꿔주기)
"""
import sys
input = sys.stdin.readline

def solution(users, emoticons):
    answer = []
    return answer


if __name__ == "__main__":
    users = [[40, 10000], [25, 10000]]
    emoticons = [7000, 9000]
    result = solution(users, emoticons)
    print(result)