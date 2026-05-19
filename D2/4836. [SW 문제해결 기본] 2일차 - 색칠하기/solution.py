import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    # 격자 만들기
    matrix = [[0]*10 for _ in range(10)]

    # 총 페인트 횟수 N, 각 페인트 배열 입력받기
    N = int(input())
    paints = [list(map(int, input().split())) for _ in range(N)]

    # 총 횟수만큼 칠하기
    for i in range(N):
        for j in range(paints[i][0], paints[i][2]+1):
            for k in range(paints[i][1], paints[i][3]+1):
                # 그 색깔이 칠해져있지 않으면 칠하기
                if matrix[j][k] != paints[i][4]:
                    matrix[j][k] += paints[i][4]

    # 보라색 칸 count
    count = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                count += 1

    print(f"#{t} {count}")