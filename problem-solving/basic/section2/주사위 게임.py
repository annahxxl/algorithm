n = int(input())
res = 0

for i in range(n):
  nums = input().split()
  nums.sort()
  a, b, c = map(int, nums)
  if a == b and b == c:
    money = 10000 + a * 1000
  elif a == b or a == c:
    money = 1000 + a * 100
  elif b == c:
    money = 1000 + b * 100
  else:
    money = c * 200
  if money > res:
    res = money

print(res)