import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def odd_sum(n):
    for i in range(1, n+1):
        input_data_list = list(map(int, input().split()))
        result = []
        for j in range(len(input_data_list)):
            if input_data_list[j]%2 == 1:
                result.append(input_data_list[j])
        print(f"#{i} {sum(result)}")
        
odd_sum(T)