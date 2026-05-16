# 100x100 2차원 배열의 행, 열, 대각선 합 중 최댓값을 구하는 문제
# 대각선 1, 2의 합을 구하는 도중 초기값을 루프 안에 넣어 계속 초기화 하는 실수했음.

import sys
sys.stdin = open("input.txt", "r")

T = 10

for _ in range(T):
    # 테스트 케이스 번호 입력
    t = int(input())
    
    # 2차원 배열 초기화
    matrix = [list(map(int, input().split())) for _ in range(100)]

    # 최댓값(답)이 될 변수
    max_value = 0

    # 행의 합
    for i in range(100):
        row_sum = sum(matrix[i])
        max_value = max(max_value, row_sum)

    # 열의 합
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += matrix[j][i]
        max_value = max(max_value, col_sum)

    # 정방향 대각선의 합
    diagonal1_sum = 0
    for i in range(100):
        diagonal1_sum += matrix[i][i]
        max_value = max(max_value, diagonal1_sum)

    # 역방향 대각선의 합
    diagonal2_sum = 0
    for i in range(100):
        diagonal2_sum += matrix[i][99-i]
        max_value = max(max_value, diagonal2_sum)

    print(f"#{t} {max_value}")
