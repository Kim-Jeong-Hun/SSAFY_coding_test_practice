# 재귀 자체는 쉽지만
# 점화식 짜는 게 직관적이지 않아 매우 어려웠던 문제
# DP 버전

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    n = N//10
    dp = [0]*(n+2)
    dp[1], dp[2] = 1, 3

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]*2

    print(f"#{t} {dp[i]}")