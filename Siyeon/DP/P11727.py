"""
세로길이는 무조건 2임
가로길이만 n으로 입력으로서 주어짐
채우는 방법은 총 3가지: 1x2(2개), 2x1, 2x2
직사각형 최소로 쓰는 방법이 아니라 그냥 방법의 수를 차곡차곡 쌓으면됨
"""
import sys

input = sys.stdin.readline
NUM = 10007

n = int(input())
dp = [0 for _ in range(n + 1)]
dp[0] = 1
dp[1] = 1


def solution():
    # 2까지 채우는 방법
    # 1)0까지 채우는 방법 + 2칸 채우는방법(2가지)
    # 2)1까지 채우는 방법 + 1칸 채우는 방법(1가지)
    for i in range(2, n + 1):
        dp[i] = (dp[i - 2]*2) + (dp[i - 1])
        if dp[i] > NUM:
            dp[i] //= NUM


solution()
print(dp[n])
