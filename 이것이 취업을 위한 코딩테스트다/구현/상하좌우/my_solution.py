import sys
sys.stdin = open("input.txt", "r")

N = int(input())
directions = list(input().split())

# x좌표, y좌표
x, y = 1, 1

for i in (directions):
    if(i == "L"):
        if(y > 1):
            y -= 1
    elif(i == "R"):
        if(y < N):
            y += 1
    elif(i == "U"):
        if(x > 1):
            x -= 1
    elif(i == "D"):
        if(x < N):
            x += 1

print(x, y)

"""
이 방식은 이 문제 해결 자체에는 효율적이지만,
확장성이 떨어지며, 여러 가지 알고리즘에서 사용할 수 있는 방식이 아님.
따라서, 방향을 배열로 저장해서 사용하는 패턴을 외워서 사용하는 것을 권장.
일반화 가능한 패턴을 사용하면 여러 가지 문제(DFS, BFS)에서 같은 패턴으로 풀이 가능
"""