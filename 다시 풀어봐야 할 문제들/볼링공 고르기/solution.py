# 그리디 방법으로 다시 풀어보기

import sys
sys.stdin = open("input.txt", "r")

def select_bowling_ball():
    N, M = map(int, input().split())
    balls = list(map(int, input().split()))
    
    # 볼링공 갯수 카운트
    ball_count = 0
    
    for i in range(N):
        for j in range(i, N):
            if balls[i] != balls[j]:
                ball_count += 1
    
    return ball_count

print(select_bowling_ball())
print(select_bowling_ball())