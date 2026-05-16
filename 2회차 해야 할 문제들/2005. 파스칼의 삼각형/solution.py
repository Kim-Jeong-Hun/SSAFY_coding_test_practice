# 파스칼의 삼각형
# 가변적인 2차원 배열 구현과 점화식을 잘 이용해야 하는 문제
# 배열 선언, 엣지케이스 처리, 점화식 활용, 출력형태까지
# 전부 복습해야 하는 문제

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def pascal_triangle():
    N = int(input())

    # 값을 저장하기 위한 2차원 배열 선언
    matrix = [[0] * (i+1) for i in range(N)]

    # N행 반복
    for i in range(N):
        # 각 행의 길이만큼 반복
        for j in range(i+1):
            # 각 행의 양 끝의 경우에는 1을 할당
            if j == 0 or j == i:
                matrix[i][j] = 1
            # 양 끝 인덱스가 아닌 경우 점화식대로 이전 행의 왼쪽과 오른쪽을 더해서 할당
            else:
                matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

    for i in range(N):
        for j in range(i+1):
            print(matrix[i][j], end=" ")
        print("")

for t in range(1, T+1):
    print(f"#{t}")
    pascal_triangle()