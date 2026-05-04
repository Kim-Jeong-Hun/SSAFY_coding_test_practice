# 구현 문제
# 정답지 보지 말고 다시 풀기

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def solution():
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    
    # 오, 아, 왼, 위 순서
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c, d = 0, 0, 0
    
    for num in range(1, N*N + 1):
        matrix[r][c] = num
        
        # 다음 칸 미리 계산
        nr, nc = r + dr[d], c + dc[d]
        
        # 다음 칸이 유효하지 않으면 방향 전환
        if not (0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 0):
            d = (d + 1) % 4
            nr, nc = r + dr[d], c + dc[d]
        
        r, c = nr, nc
    
    return matrix

print(solution())