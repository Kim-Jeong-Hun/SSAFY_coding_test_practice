import sys
sys.stdin = open("input.txt", "r")

from collections import Counter

T = int(input())

for _ in range(1, T+1):
    t_num = int(input())
    array = list(map(int, input().split()))
    result = Counter(array).most_common(1)
    print(f"#{t_num} {result[0][0]}")