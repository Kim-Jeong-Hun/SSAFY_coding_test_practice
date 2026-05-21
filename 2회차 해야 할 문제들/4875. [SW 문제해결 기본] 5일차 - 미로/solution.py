import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    # 시작점 찾기
    sx, sy = 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                sx, sy = i, j

    # 방향 배열 초기화
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # dfs 로직
    # 1. 각 결정 = 매번 지금 위치에서 어느 방향으로 갈 지 결정
    # 2. 함수 하나의 호출 = 지금 어느 한 칸에 서 있는 상황을 처리하는 단계
    # 3. 이 결정 시점에서 알아야 하는 것(인자) = 지금 어디에 있는지 (x, y)
    # 4. 언제 끝나고, 끝날때 뭘 하지? = 도착점일 때 1리턴, 도착점 없으면 0리턴
    # 5. 한 결정 안에서 선택해야 하는 것(상태 복원이 필요한가?) = 이웃된 4방향으로 좌표, 갈 수 있는 곳으로 dfs 호출

    # 3번 (x,y(위치정보)가 필요함)
    def dfs(x, y):
        # 4번 (matrix[x][y]가 3일 때 끝나고, 끝날 때 1리턴)
        if matrix[x][y] == 3:
            return 1

        # 2번 (방문을 표시하고, 조건에 맞으면 방문)
        visited[x][y] = True

        # 4방향이므로 4번 반복
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            # 조건 : nx, ny가 배열 범위 내에 있어야 하고, 방문하지 않은 곳이어야 하며, 벽(1)이 아니어야 함.
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and matrix[nx][ny] != 1:
                # 이웃이 도착점 갈 수 있다고 하면, 나도 갈 수 있음. (길이 이어져 있으므로)
                if dfs(nx, ny) == 1:
                    return 1

        # 4방향 전부 시도하고도 도착점을 찾지 못하면
        return 0

    print(f"#{t} {dfs(sx, sy)}")