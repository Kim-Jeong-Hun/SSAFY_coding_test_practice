T = int(input())

def find_average(n):
    for i in range(1, n+1):
        data_list = list(map(int, input().split()))
        print(f"#{i} {round(sum(data_list)/len(data_list))}")
    
print(find_average(T))