'''
# my solution (시간 초과)
n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n):
  for j in range(n):
    if sum(lst[i:j+1]) == m:
      cnt += 1
print(cnt)
'''

# other solution: index 포인터를 이용한 모든 경우의 수 구하기
n, m = map(int, input().split())
lst = list(map(int, input().split()))
tot = lst[0]
lp = rp = cnt = 0
while True:
  if tot < m:
    rp += 1
    if rp == n:
      break
    tot += lst[rp]
  elif tot == m:
    cnt += 1
    tot -= lst[lp]
    lp += 1
  else:
    tot -= lst[lp]
    lp += 1
print(cnt)