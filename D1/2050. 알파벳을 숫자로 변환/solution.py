# 다시 풀어봐야 하는 문제

# - 몰랐던 것
# 소문자 a의 아스키코드 값 : 97
# 대문자 A의 아스키코드 값 : 65
# 1의 아스키코드 값 : 1
# ord()는 문자를 아스키코드 값으로 변경해주는 함수
# chr()은 아스키코드 값을 문자로 변경해주는 함수

text = input().upper()

for i in text:
    result = ord(i) - 64
    print(result, end=" ")