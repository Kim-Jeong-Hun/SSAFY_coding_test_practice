import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    # 숫자 저장 배열 matrix, 방문 확인 배열 visited
    matrix = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    
    # 방향 배열 [우, 하, 좌, 상] 순서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 방향
    direction = 0

    # 넣을 숫자
    number = 1

    # 시작점
    x = 0
    y = 0

    # NxN번 반복 필요
    # 만약 경계 범위를 넘어가거나 방문한 곳이면 방향 전환
    while number != (N*N)+1:
        if 0 <= x < N and 0 <= y < N and visited[x][y] == 0:
            visited[x][y] = 1
            matrix[x][y] = number
            number += 1
        else:
            x, y = x-dx[direction], y-dy[direction]
            direction = (direction+1)%4
        x, y = x+dx[direction], y+dy[direction]

    print(f"#{t}")
    for i in range(N):
        print(*matrix[i])