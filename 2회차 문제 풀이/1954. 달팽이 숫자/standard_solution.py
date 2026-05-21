import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]

    # 방향 정의
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 시작 좌표, 시작 방향
    x, y = 0, 0
    direction = 0

    for num in range(1, (N*N)+1):
        matrix[x][y] = num
        # 임시 좌표 nx, ny
        nx, ny = x+dx[direction], y+dy[direction]

        # 임시 좌표가 조건에 부합하지 않는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx][ny] != 0:
            # 방향 바꿔서 재계산
            direction = (direction+1)%4
            nx, ny = x+dx[direction], y+dy[direction]
        # 최종 반영
        x, y = nx, ny

    print(f"{t}")
    for i in range(N):
        print(*matrix[i])