"""
패턴화 가능한 권장 답안
"""

N = int(input())
plans = input().split()
x, y = 1, 1

# L, R, U, D에 따른 이동 방향
# dx, dy, move_types의 각 index가 일치하도록 하는 것이 중요
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 지도의 경계를 넘어서는 경우 최종 x, y에 더하지 않고 버리기
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny
    
print(x, y)