n = int(input())

def factorial(n):
  res = 1
  if n == 0:
    return 1
  for num in range(1, n+1):
    res *= num
  return res

print(factorial(n))