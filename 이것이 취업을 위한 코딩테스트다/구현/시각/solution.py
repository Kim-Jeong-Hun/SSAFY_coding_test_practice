# 복습 필요

import sys
sys.stdin = open("input.txt", "r")

# 시간 입력 받기
N = int(input())
count = 0

# 만약 N이 23이면 0부터 23까지 24개의 경우를 알아야 함
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if('3' in str(i)+str(j)+str(k)):
                count += 1
                
print(count)


# 이 문제는 완전 탐색(Brute Force) 문제로, 
# 확인해야 할 데이터의 개수가 100만 개 이하일 때 완전 탐색을 사용하면 적절하다.