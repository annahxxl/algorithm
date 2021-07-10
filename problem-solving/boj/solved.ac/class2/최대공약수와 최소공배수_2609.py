a, b = map(int, input().split(' '))

# 유클리드 호제법으로 최대공약수 구하기
def gcd(a, b):
  r = a % b
  while r > 0:
    a = b
    b = r
    r = a % b
  return b
    
# 최소공배수 구하기    
def lcm(a, b):
  return a*b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))