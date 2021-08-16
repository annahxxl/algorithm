'''
# 반복문을 이용한 풀이
n = int(input())
a, b = 0, 1
while n > 0:
  a, b = b, a+b
  n -= 1
print(a)
'''

'''
# 아래의 풀이는 재귀 함수 호출이 깊이가 깊어질수록 2배로 중가 하기 때문에 시간 복잡도 O(2**n)이므로 시간 초과
def fibo(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibo(n-1) + fibo(n-2)
print(fibo(int(input())))
'''

# 다이나믹 프로그래밍을 이용한 풀이
dp = [0] * 46
dp[1] == 1
def fibo(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  if dp[n] != 0:
    return dp[n]
  else:
    dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]
print(fibo(int(input())))