import sys
sys.stdin = open("input.txt", "r")

for _ in range(1, 11):
    t = int(input())

    # 행렬은 16*16 고정
    matrix = [list(map(int, input())) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]

    # 이 문제에서 갈 수 있는 방향은 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작점 찾기
    sx, sy = 0, 0
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                sx, sy = i, j

    # 길찾기 프로그램
    def dfs(x, y):
        # 도착점이 3인 경우 1리턴
        if matrix[x][y] == 3:
            return 1

        # 아닌 경우 계속 수행
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False and matrix[nx][ny] != 1:
                visited[nx][ny] = True
                if dfs(nx, ny) == 1:
                    return 1
        # 모든 경우에서 도착점을 찾지 못하면 0 리턴
        return 0

    print(f"#{t} {dfs(sx, sy)}")