"""
처음에 풀다가 5+7+5 = 5+5+7 = 7+5+5 모두 같은데, 이게 서로 다르다고 자꾸 구분을 해서 헤맸음
나는 1~금액까지 돌면서 그 안에서 동전별로 값을 구했는데, 이러니까 문제가 있었음
반대로 동전들을 기준으로 금액을 돌면 괜찮음. 뭔소리냐면 5만 사용해서 금액을 쭉 돌고,
그렇게 해서 나온 dp를 계승받아서 7을 이용해서 금액을 쭉 돌고 하는거임. -> 이렇게 하면 5는 7의 존재를 모르기 때문에 애초에 5+7+5라던지, 7+5+5따위가 생기지 않음
조합이 아예 생기지 않도록 하는거! 충격임..
"""
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    money = int(input())
    
    dp = [0 for _ in range(money+1)]
    dp[0] = 1

    for coin in coins:
        for i in range(coin, money+1):
                dp[i] += dp[i-coin]
            
    print(dp[money])
