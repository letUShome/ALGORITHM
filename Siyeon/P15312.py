#동그란 순환구조로 되어있는거를 해결하는 방법은 0포함+마지막 미포함 / 0미포함+마지막 포함 둘로 나눠서 함수를 만들면 됨
#동전줍기인데 연속으로 줍지못하는 그 문제랑 결이 비슷함
#dp[i]가 무조건 i번째 money를 줍는 경우를 저장하겠다고 생각하지말고, 그냥 그 집까지 고려했을때 최선의 선택이 무엇이었는지를 담는다고 생각하면 좋음

import copy
def zeroInclude(money):
    dp = [0 for i in range(len(money))]
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, len(money)):
        if i == len(money) - 1:
            dp[i] = dp[i - 1]
            continue

        if money[i] + dp[i - 2] > dp[i - 1]:
            dp[i] = money[i] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]

    return dp[len(money) - 1]


def zeroExclude(money):
    dp = [0 for i in range(len(money))]
    dp[1] = money[1]
    dp[2] = max(money[1], money[2])

    for i in range(3, len(money)):
        if money[i] + dp[i - 2] > dp[i - 1]:
            dp[i] = money[i] + dp[i - 2]
        else:
            dp[i] = dp[i - 1]

    return dp[len(money) - 1]


def solution(money):
    answer = max(zeroInclude(money), zeroExclude(money))
    return answer