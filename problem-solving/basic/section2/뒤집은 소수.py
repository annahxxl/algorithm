'''
# my solution
n = int(input())
nums = list(input().split())

def reverse(x):
  num = x[::-1]
  return int(num)
  
def isPrime(x):
  if x == 1:
    return False
  for i in range(2, x):
    if x % i == 0:
      return False
  return True

for num in nums:
  num = reverse(num)
  if isPrime(num):
    print(num, end=' ')
'''

# other solution
n = int(input())
nums = list(map(int, input().split()))

def reverse(x):
  res = 0
  while x > 0:
    r = x % 10
    res = (res * 10) + r
    x = x // 10
  return res
  
def isPrime(x):
  if x == 1:
    return False
  for i in range(2, x//2+1): # 1과 자기 자신을 뺀 약수 체크
    if x % i == 0:
      return False
  return True

for x in nums:
  tmp = reverse(x)
  if isPrime(tmp):
    print(tmp, end=' ')