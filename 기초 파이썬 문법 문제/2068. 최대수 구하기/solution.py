import sys
sys.stdin = open("input.txt", "r")

# 10개의 수를 입력받아, 그 중에서 가장 큰 수를 출력하는 프로그램
# 그냥 수를 전부 받아서 리스트로 만들고,
# max() 때리면 끝인듯 -> max()는 사용 불가능
# 그럼 리스트 정렬해서 마지막 값 꺼내면 될 듯

T = int(input())

def find_max(n):
    data_list = list(map(int, input().split(' ')))
    data_list.sort()
    result = data_list.pop()
    return print(f"#{n} {result}")
    
for i in range(1, T+1):
    find_max(i)