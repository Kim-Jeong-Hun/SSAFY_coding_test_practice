# 그리디 연습하기 좋은 문제인듯

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(T):
    # A, B, N 받기
    A, B, N = map(int, input().split())
    
    # 결과값
    count = 0
    
    # 만약 A가 10, B가 7이다
    # 처음에는 7 += 10
    # 두번째는 10 += 17
    # 세번째는 17 += 27
    # 네번째는 27 += 44
    while A <= N and B <= N:
        if A < B:
            A += B
        else:
            B += A
        count += 1
    
    print(count)