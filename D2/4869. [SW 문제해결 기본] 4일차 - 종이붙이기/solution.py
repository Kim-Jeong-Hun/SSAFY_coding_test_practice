# 재귀 자체는 쉽지만
# 점화식 짜는 게 직관적이지 않아 매우 어려웠던 문제
# 재귀함수 버전

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    def rec(length):
        if length == 10:
            return 1
        if length == 20:
            return 3
        return rec(length-10) + 2*rec(length-20)

    print(f"#{t} {rec(N)}")