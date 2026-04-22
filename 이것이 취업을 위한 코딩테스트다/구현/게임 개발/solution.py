# 코드가 매우 길고 복잡하다.
# 선언해야 할 변수도 많고, 할당해야 할 것도 많다.
# 먼저 필요한 모든 것들을 선언해놓은 뒤에 시뮬레이션하는 것이 중요
# 풀이를 이해한 후, 다시 풀기
# 너무 어렵고 이해가 안된다.

import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visited = [[0] * M for _ in range(N)]

# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

# 현재 캐릭터가 서 있는 좌표 방문처리
visited[x][y] = 1

# 전체 맵 정보를 입력받기
game_map = []
for i in range(N):
    game_map.append(list(map(int, input().split())))
    
# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수 정의
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
# 처음 서있던 장소를 방문한 것으로 처리했으므로 count=1 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 육지이면서 가보지 않은 칸이 존재하는 경우 이동
    if visited[nx][ny] == 0 and game_map[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = x - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)