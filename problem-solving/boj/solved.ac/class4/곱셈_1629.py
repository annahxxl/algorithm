# 분할 정복

def solve(a, b):
  if b == 1:
    return a % c
  else:
    tmp = solve(a, b//2)
    if b % 2 == 0: # 짝수일 경우
      return tmp * tmp % c
    else: # 홀수일 경우
      return tmp * tmp * a % c

if __name__ == '__main__':
  a, b, c = map(int, input().split())
  print(solve(a, b))