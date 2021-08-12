'''
# my solution
n = int(input())
nums = list(input().split())
sums = list() # 자릿수의 합

def digit_sum(x):
  sum = 0
  for i in x:
    sum += int(i)
  return sum

for num in nums:
  result = digit_sum(num)
  sums.append(result)
MAX = max(sums)
for i in range(n):
  if sums[i] == MAX:
    print(nums[i])
'''

# other solution
n = int(input())
nums = list(map(int, input().split()))

def digit_sum(x):
  sum = 0
  while x > 0:
    sum += x % 10
    x = x // 10
  return sum

MAX = -2147000000
for x in nums:
  sum = digit_sum(x)
  if sum > MAX:
    MAX = sum
    res = x
print(res)