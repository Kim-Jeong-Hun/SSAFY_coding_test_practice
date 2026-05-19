import sys
sys.stdin = open("input.txt", "r")

def rec(i, N, M):
    # 만약 index가 끝에 다다르면 리턴
    if i == M:
        return N
    # 아니면 재귀호출
    else:
        return N * rec(i+1, N, M)

for _ in range(10):
    t = int(input())
    N, M = map(int, input().split())

    print(f"#{t} {rec(1, N, M)}")