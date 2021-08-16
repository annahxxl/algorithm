'''
# 재귀 함수를 이용한 풀이 (Python3 - 시간 초과)
import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
result = 0
def solve(n, x, y):
  global result
  if n == 2:
    if x == r and y == c:
      print(result)
      return
    result += 1
    if x == r and y+1 == c:
      print(result)
      return
    result += 1
    if x+1 == r and y == c:
      print(result)
      return
    result += 1
    if x+1 == r and y+1 == c:
      print(result)
      return
    result += 1
    return
  solve(n/2, x, y)
  solve(n/2, x, y + n/2)
  solve(n/2, x + n/2, y)
  solve(n/2, x + n/2, y + n/2)
solve(2**n, 0, 0)
'''

# 반복문을 이용한 풀이
n, r, c = map(int, input().split())
cnt = 0
while n > 1:
  size = (2**n) // 2 # 4분할로 나누었을 때의 한 변의 크기
  if r < size and c < size: # 2사분면
    pass
  elif r < size and c >= size: # 1사분면
    cnt += size ** 2
    c -= size
  elif r >= size and c < size: # 3사분면
    cnt += size ** 2 * 2
    r -= size
  elif r >= size and c >= size: # 4사분면
    cnt += size ** 2 * 3
    r -= size
    c -= size
  n -= 1
if r == 0 and c == 0:
  print(cnt)
if r == 0 and c == 1:
  print(cnt + 1)
if r == 1 and c == 0:
  print(cnt + 2)
if r == 1 and c == 1:
  print(cnt + 3)