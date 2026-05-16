# 매우 좋은 문제라고 생각함.
# 이 문제는 두 가지 조건을 찾는 것이 중요함.
# 조건 1 : 초기값이 2미만이면 더하는 것이 곱하는 것보다 낫다.
# 초기값 1: 
#   n 곱하면 결과는 n
#   n 더하면 결과는 1+n
# 초기값 0: 
#   n 곱하면 결과는 0
#   n 더하면 결과는 n
# 초기값 음수:
#   n 곱하면 결과는 음수의 n배
#   n 더하면 결과는 음수+n
# 조건 2 : 초기값 이후 곱하는 수가 2미만이면 더하는 것이 곱하는 것보다 낫다.

import sys
sys.stdin = open("input.txt", "r")

def times_or_plus():
    S = input()
    
    total = int(S[0])
    
    for i in range(1, len(S)):
        # 조건 1. 초기값이 2보다 작으면 더하기
        if total < 2 :
            total += int(S[i])
        # 조건 2. 숫자가 2보다 작으면 더하기
        elif int(S[i]) < 2 :
            total += int(S[i])
        else:
            total *= int(S[i])
    
    return total

for j in range(2):
    print(times_or_plus())