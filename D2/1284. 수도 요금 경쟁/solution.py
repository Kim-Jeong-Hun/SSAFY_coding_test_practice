import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# P : A사의 1리터당 요금

# Q : B사의 기본 요금
# R : B사의 월간 사용량 기준
# S : 초과량 1리터당 요금

# W : 종민이가 사용하는 수도 양

for t in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())

    a_cost = P*W
    b_cost = Q

    # 사용하는 수도 양이 B사의 기준 사용량 R 이상인 경우
    if R < W:
        b_cost += (W-R)*S

    print(f"#{t} {min(a_cost, b_cost)}")