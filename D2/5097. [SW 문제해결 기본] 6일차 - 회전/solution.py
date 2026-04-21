# 기본 아이디어 : M번 만큼 직접 맨 뒤로 보내는 작업을 실시한다.
# 그런데 M번 만큼 굳이 직접 맨 뒤로 보내야 할까?
# N이 3이고, M이 10이라면, 10번 직접 회전한 것과, 1번 회전한 것의 결과는 같다. (3, 6, 9번째마다 원상태로 돌아오므로)
# 따라서 회전은 M%N 번만 하면 된다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    print(f"#{i} {array[(M%N)]}")