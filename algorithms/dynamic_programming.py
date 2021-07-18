# recursive call 활용하여 피보나치 수열 만들기
def fibo(num):
  if num <= 1:
    return num
  return fibo(num-1) + fibo(num-2)
print(fibo(4))
print(fibo(3)+fibo(2))

# 동적 계획법 활용하여 피보나치 수열 만들기
def fibo_dp(num):
  cache = [0 for _ in range(num+1)]
  cache[0] = 0
  cache[1] = 1
  for i in range(2, num+1):
    cache[i] = cache[i-1] + cache[i-2]
  return cache[num]
print(fibo_dp(10))
print(fibo_dp(9)+fibo_dp(8))