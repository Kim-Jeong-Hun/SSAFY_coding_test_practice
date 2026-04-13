# 리스트에서 중복이 제거된 리스트 출력
# -> 집합을 사용하여 중복을 제거하고 다시 "리스트로 출력"

data = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

set_data = set(data)
list_data = list(set_data)
print(list_data)