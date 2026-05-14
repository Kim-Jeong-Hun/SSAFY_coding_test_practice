# 짝 소거 문제 - 스택 사용하는 문제
# 빈 리스트를 명시적으로 분기처리하는 쪽이 실수가 더 적으므로
# 처음부터 하나의 요소를 넣어놓는 방법은 사용하지 말자!

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    S = list(input())
    new_S = []

    for i in range(len(S)):
        if len(new_S) == 0:
            new_S.append(S[i])
        elif S[i] == new_S[-1]:
            new_S.pop()
        else:
            new_S.append(S[i])

    print(f"#{t} {len(new_S)}")