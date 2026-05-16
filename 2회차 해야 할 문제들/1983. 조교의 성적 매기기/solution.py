# 로직은 잘 짜놨는데
# 계산을 이상하게 해서 틀림.
# 다시 풀면 풀릴듯

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N, K = map(int, input().split())
    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    score = []

    for _ in range(N):
        M, L, A = map(int, input().split())
        score.append((M*0.35)+(L*0.45)+(A*0.2))

    # K번째 학생의 총점 target
    target = score[K-1]
    score.sort(reverse=True)

    rank = score.index(target)
    result = rank // (N//10)
    answer = grade[result]
    print(f"#{t} {answer}")
