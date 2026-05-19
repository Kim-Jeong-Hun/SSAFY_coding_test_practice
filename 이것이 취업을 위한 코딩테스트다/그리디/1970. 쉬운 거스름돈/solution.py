import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 돈의 종류 8개
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    
    # 각 단위의 카운트 배열
    counts = [0]*8

    for i in range(len(money)):
        counts[i] = N//money[i]
        N %= money[i]

    print(f"#{t}")
    print(*counts)