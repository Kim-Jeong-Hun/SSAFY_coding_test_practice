import sys
sys.stdin = open("input.txt", "r")

def sum_str():
    N = int(input())
    str1 = input()
    str2 = input()
    result = str2.count(str1)
    print(f"#{N} {result}")

for _ in range(10):
    sum_str()