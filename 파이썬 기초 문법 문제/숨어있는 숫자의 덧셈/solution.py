# 어떠한 문자열이 숫자인지 판별하는 메소드는 문자열.isdigit()이다.

import sys
sys.stdin = open("input.txt", "r")

def solution():
    my_string = input()
    answer = 0
    for i in my_string:
        if i.isdigit(): 
            answer += int(i)
    return answer

print(solution())
print(solution())