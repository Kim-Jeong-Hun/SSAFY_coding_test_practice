# D3 구현 문제
# 수확할 곳의 넓이가 증가하는 로직과 감소하는 로직으로 나누어 구현함.
# 시작점, 끝점 변수를 생각하는 습관을 항상 들일 것.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    
    # N 입력 및 2차원 배열 초기화
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    # 결과 변수
    result = 0

    # 시작점, 도착점
    start = N//2
    end = (N//2)+1

    # 수확하는 열 크기가 증가하는 로직
    for i in range(0, (N//2)+1):
        for j in range(start, end):
            result += matrix[i][j]
        start -= 1
        end += 1

    # 시작, 끝 범위 재조정
    # 증가 로직에서 더하기가 끝난 후에도 시작, 끝 점이 증감했으므로
    # 2칸씩 조정
    start += 2
    end -= 2

    # 수확하는 열 크기가 감소하는 로직
    for i in range((N//2)+1, N):
        for j in range(start, end):
            result += matrix[i][j]
        start += 1
        end -= 1

    print(f"#{t} {result}")