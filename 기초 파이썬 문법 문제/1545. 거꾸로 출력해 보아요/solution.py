# 표준 라이브러리 sys(system) import
# system의 기본 입력을 파일(읽기 형식)으로 받기
import sys
sys.stdin = open("SampleInput.txt", "r")

# 파이썬의 input 함수가 반환하는 값은 문자열 형식
# 따라서 int()로 int형으로 바꾸어줘야 함.
a = int(input())

for i in range(a, -1, -1):
    print(i, end=" ")