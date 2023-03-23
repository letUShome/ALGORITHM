# 입력
n = int(input())
# dp 배열 선언 -> n을 반드는 방법을 연산
dp = [0 for _ in range(n+1)]
# 최솟값을 만드는 숫자들을 저장
numbers = [0 for _ in range(n+1)]
dp[1] = 0

'''
1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
2) X가 2로 나누어 떨어지면, 2로 나눈다.
3) 1을 뺀다.
'''
for i in range(2, n+1):
    # 3) -1에 대한 연산
    dp[i] = dp[i-1] + 1
    # 이 숫자를 만드는 데 최솟값인 연산
    numbers[i] = i - 1

    # 1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        numbers[i] = i//3

    # 2) X가 2로 나누어 떨어지면, 2로 나눈다.
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        numbers[i] = i//2

print(dp[n])
while n != 0:
    print(n, end=' ')
    n = numbers[n]

