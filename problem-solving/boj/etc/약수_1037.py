# N 구하기
# 가장 큰값과 작은값을 곱하여 출력해준다.
cnt = int(input()) # N의 진짜 약수의 개수
nums = list(map(int, input().split())) # N의 진짜 약수들 (1과 N을 제외한 약수들)

max_num = max(nums)
min_num = min(nums)

print(max_num * min_num)