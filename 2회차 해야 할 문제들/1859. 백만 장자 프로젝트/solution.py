# 쟁여놓는 매커니즘을 모르겠어서 답안 확인
# 뒤에서부터 인덱스를 접근하는 방식이 있음. (최적화 방법)
# 문제의 의도를 따르자면 앞에서부터 접근하는 방식 사용 필요.
# 그리디 알고리즘이긴한데, 풀이방법을 모르면 많이 어렵다는 평가.

# 1. 배열중 가장 큰 값을 찾고 그 값보다 앞에 있는 값들과 차이만큼 결과값에 ++ 합니다.
# 2. 그 후, 가장 큰 값과 앞에 있는 값들을 모두 배열에서 제외한 새로운 배열을 만듭니다.
# 배열의 크기가 0이나 1이 될 때까지 1, 2 반복

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def max_margin():
    N = int(input())
    prices = list(map(int , input().split()))
    result = 0
    
    while len(prices) != 0:
        idx_max = max(prices)
        now = prices.index(idx_max)
        imci = prices[:now]
        prices = prices[now+1:]
        for i in range(len(imci)):
            result += idx_max - imci[i]
    
    return result

for j in range(1, T+1):
    print(f"#{j} {max_margin()}")