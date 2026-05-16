import sys
sys.stdin = open("input.txt", "r")

# 세로, 가로 입력받기
N, M = map(int, input().split())

matrix = []
for _ in range(N):
    array = list(map(int, input()))
    matrix.append(array)

# dfs 만들기
def dfs(x, y):
    # 제약조건을 넘어가면 False
    # x는 행, y는 열
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # matrix의 x행의 y열을 방문하지 않았다면,
    # 방문 처리
    if matrix[x][y] == 0:
        matrix[x][y] = 1
        # x, y의 상하좌우도 방문
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1

print(result)