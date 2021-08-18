'''
# my solution
n = int(input())
money = list()
for _ in range(n):
  nums = list(map(int, input().split()))
  dic = dict()
  for num in nums:
    if num not in dic:
      dic[num] = 1
    else:
      dic[num] += 1
  for key, value in dic.items():
    if value == 3:
      result = 10000 + key * 1000
    elif value == 2:
      result = 1000 + key * 100
    else:
      result = max(nums) * 100
    money.append(result)
print(max(money))
'''

# other solution
n = int(input())
MAX = 0
for _ in range(n):
  nums = sorted(list(map(int, input().split())))
  a, b, c = nums
  if a==b and b==c:
    money = 10000 + a * 1000
  elif a==b or a==c:
    money = 1000 + a * 100
  elif b==c:
    money = 1000 + b * 100
  else:
    money = c * 100
  if money > MAX:
    MAX = money
print(MAX)