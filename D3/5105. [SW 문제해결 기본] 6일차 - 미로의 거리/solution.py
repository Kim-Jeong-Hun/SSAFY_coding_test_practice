from collections import deque
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]

    # 방문 확인용 배열
    visited = [[False] * N for _ in range(N)]

    # 거리 저장용 배열
    dist = [[0] * N for _ in range(N)]

    # 주변(상하좌우) 이동하기 위한 배열
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작점 찾기
    sx, sy = 0, 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                sx, sy = i, j

    q = deque()
    visited[sx][sy] = True
    q.append((sx, sy))

    # 답 변수 초기화
    answer = 0

    while q:
        x, y = q.popleft()
        if matrix[x][y] == 3:
            answer = dist[x][y] - 1

        for d in range(4):
            # x, y에서 상하좌우를 계산한 임시 좌표 만들기
            nx, ny = x + dx[d], y + dy[d]
            # 임시 좌표가 모든 조건을 통과한다면
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and matrix[nx][ny] != 1:
                # 방문 처리, 거리 계산을 하고 큐에 저장
                visited[nx][ny] = True
                # 지금(x, y)까지의 거리에 1 추가됨.
                dist[nx][ny] = dist[x][y] + 1
                # 큐에 저장
                q.append((nx, ny))

    print(f"#{t} {answer}")