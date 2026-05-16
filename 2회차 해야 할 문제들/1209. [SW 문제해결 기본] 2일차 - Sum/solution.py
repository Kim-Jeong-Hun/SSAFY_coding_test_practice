# 파이썬스러운 표현을 사용하면 코드를 크게 줄일 수 있음.
# 다시 풀어보기

import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    # 테스트 케이스 번호 읽기
    tc = int(input())

    # 2차원 배열 선언 및 할당
    matrix = []
    for _ in range(100):
        arr = list(map(int, input().split()))
        matrix.append(arr)

    # 최댓값
    result = 0
    total1 = 0
    total2 = 0

    # 행의 합
    for i in range(100):
        row_total = sum(matrix[i])
        if row_total > result:
            result = row_total

    # 열의 합
    for j in range(100):
        col_total = sum([matrix[k][j] for k in range(100)])
        if col_total > result:
            result = col_total

    # 대각선 1의 합
    for a in range(100):
        total1 += matrix[a][a]
    if total1 > result:
        result = total1

    # 대각선 2의 합 (행은 커지고, 열은 줄어듬)
    for b in range(100):
        total2 += matrix[b][99-b]
    if total2 > result:
        result = total2

    print(f"#{t} {result}")