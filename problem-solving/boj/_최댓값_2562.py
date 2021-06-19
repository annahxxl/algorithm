nums = list()
max_num = 0

for _ in range(9):
  num = int(input())
  nums.append(num)

for num in nums:
  if num > max_num:
    max_num = num

print(max_num)
print(nums.index(max_num)+1)