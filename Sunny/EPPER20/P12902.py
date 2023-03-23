# 세로 길이 = 3 & 가로 길이 = n
# 세로 길이 = 1 & 가로 길이 = 2
# 가로길이가 홀수일때 채울 수 있는 방법이 없음
def solution(n):
    answer = 0
    mod = 1000000007

    dp = [0 for _ in range(n + 1)]
    dp[2] = 3

    if n > 2:
        dp[4] = 11

        for i in range(6, n + 1):
            if i % 2 != 0:
                continue
            else:
                dp[i] = dp[i - 2] * 3 + 2
                for j in range(i - 4, -1, -2):
                    dp[i] += dp[j] * 2
                dp[i] = dp[i] % mod

    return dp[n]