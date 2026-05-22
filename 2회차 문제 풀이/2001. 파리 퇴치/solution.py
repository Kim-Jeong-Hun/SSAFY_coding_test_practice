import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    # 파리채가 순회하는 횟수
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 각 영역만큼의 파리 수를 구하기 위한 변수
            flies = 0
            # 각 파리채의 영역
            for k in range(i, i+M):
                for l in range(j, j+M):
                    flies += matrix[k][l]
            max_value = max(flies, max_value)

    print(f"#{t} {max_value}")