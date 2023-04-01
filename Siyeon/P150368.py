"""
목표: 플러스 가입자 수 증가 > 판매액을 최대로
구입: 특정 할인율 이상일때 -> 총합이 특정이상이면 플러스 가입

1. 일단 원하는 할인율 이상으로 할인하여 다 담게 하고, 그로인해 제한을 넘게 만드는게 목표
2. 1번을 충족하기 위해서는 가장 높은 할인율을 원하는 유저에 맞춰서 할인해봐야할듯
3. 거기서 할인율이 더 낮으면서 한계치를 못넘은 사람들을 유인하기 위해 그들에 맞춰서 할인율을 한두개 내려보기
4. 3번에서 버는돈을 최대화하기 위해 원하는 할인율에 딱 맞춰서 내려보자 (할인율은 40, 30, 20, 10으로 존재함)

이모티콘은 최대 7개므로 할인율까지 하면 28개, 거기서 하나씩 선택해서 나오는 확율은 16000쯤
그러니까 그냥 하나하나 다 완탐해서 고르자
"""
import sys
input = sys.stdin.readline
INF = sys.maxsize
fixed_users = []
emoji = []
rates = [40, 30, 20, 10]
answer = [0, 0]


def fixRate(users):
    for i, user in enumerate(users):
        rate = user[0]

        if 30 < rate < 40:
            users[i][0] = 40
        elif 20 < rate < 30:
            users[i][0] = 30
        elif 10 < rate < 20:
            users[i][0] = 20
        elif rate < 10:
            users[i][0] = 10
    return users


def calculate(discount):
    global answer
    if len(discount) == len(emoji):
        plus, total = 0, 0

        for rate, limit in fixed_users:
            money = 0

            for i, r in enumerate(discount):
                if r >= rate:
                    money += emoji[i]*(100-r)//100
            if money >= limit:
                plus += 1
            else:
                total += money

        if answer[0] < plus:
            answer = [plus, total]
        elif answer[0] == plus and answer[1] < total:
            answer = [plus, total]

        return

    for rate in rates:
        discount.append(rate)
        calculate(discount)
        discount.pop()


def solution(users, emoticons):
    global fixed_users, emoji, answer
    fixed_users = fixRate(users)
    emoji = emoticons

    calculate([])

    return answer


if __name__ == "__main__":
    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    result = solution(users, emoticons)
    print(result)
