# 백트래킹 문제
# 코드만 써보고 넘어가기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    visited_col = [False]*N
    # 백트래킹을 위해서 필요한 조건
    # 모든 row, col 방문 시 종료
    # 첫 시작점 = 0,0
    # 첫 시작값 = 100*N
    min_sum = 100*N

    def backtrack(row, total):
        global min_sum

        if row == N:
            min_sum = min(min_sum, total)
            return

        # 가지치기
        if total >= min_sum:
            return

        # 그 열을 방문하지 않았다면 방문 가능
        for col in range(N):
            if visited_col[col] == False:
                # 해당 열 방문 처리
                visited_col[col] = True
                # total에 해당 행열 더하기
                total += matrix[row][col]
                backtrack(row+1, total)

                # 더한 값, 방문 흔적 복원
                total -= matrix[row][col]
                visited_col[col] = False

    backtrack(0, 0)

    print(f"#{t} {min_sum}")
