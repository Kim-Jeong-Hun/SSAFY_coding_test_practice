import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    # 덤프 횟수 N
    N = int(input())

    # 각 상자의 높이
    H = list(map(int, input().split()))

    for i in range(N):
        # 가장 높은 상자와 가장 낮은 상자 찾기
        highest_i, lowest_i = H.index(max(H)), H.index(min(H))
        H[highest_i] -= 1
        H[lowest_i] += 1

    # 모든 덤프 작업 이후의 가장 높은 상자와 가장 낮은 상자 찾기
    now_highest_i, now_lowest_i = H.index(max(H)), H.index(min(H))
    print(f"#{t} {H[now_highest_i] - H[now_lowest_i]}")