import sys
sys.stdin = open("input.txt", "r")

T = int(input())
score_list = list(map(int, input().split(' ')))
m = len(score_list) // 2
# .sort() 함수는 리턴값이 없음. 조심
score_list.sort()
print(score_list[m])