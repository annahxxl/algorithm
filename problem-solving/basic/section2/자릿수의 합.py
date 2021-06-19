n = int(input())
nums = list(map(int, input().split()))
max = 0

def digit_sum(x):
  sum = 0
  while x > 0:
    sum += x % 10
    x = x // 10
  return sum

for num in nums:
  sum = digit_sum(num)
  if sum > max:
    max = sum
    res = num
    
print(res)