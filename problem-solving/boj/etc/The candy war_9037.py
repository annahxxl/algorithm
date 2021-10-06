def is_same(n, c):
  for i in range(n):
    if c[i] % 2 == 1:
      c[i] += 1
  return len(set(c)) == 1

def turn(n, c):
  tmp = [0 for _ in range(n)] # 오른쪽으로 넘겨줘야 하는 사탕의 개수 리스트
  for idx in range(n):
    c[idx] //= 2
    tmp[(idx + 1) % n] = c[idx]
  for idx in range(n):
    c[idx] += tmp[idx]
  return c

def solution():
  n, c = int(input()), list(map(int, input().split()))
  cnt = 0
  while not is_same(n, c):
    cnt += 1
    c = turn(n, c)
  print(cnt)

for _ in range(int(input())):
  solution()