n, k = map(int, input().split())
dp = [[0]*201 for _ in range(201)] # dp[n][k]
for i in range(1, 201):
    dp[1][i] = i
    dp[i][1] = 1
for i in range(2, k+1):
    for j in range(2, n+1):
        dp[j][i] = (dp[j-1][i] + dp[j][i-1]) % 1000000000
print(dp[n][k])






'''
n    k
     1 2 3 4
1    1 2 3 4
2    1 3 6 10
3    1 
4    1
'''