n, c = map(int, input().split())
loc = []

for _ in range(n):
  loc.append(int(input()))
  
loc.sort()

def count(len): # 마구간에 배치할 수 있는 말 수 구하기
  cnt = 1
  ep = loc[0] # 말이 마지막으로 배치된 마구간 위치 (endpoint)
  for i in range(1, n):
    if loc[i]-ep >= len:
      cnt += 1
      ep = loc[i]
  return cnt

lp = 1
rp = loc[n-1]

while lp <= rp:
  mid = (lp+rp) // 2
  if count(mid) >= c:
    res = mid
    lp = mid + 1
  else:
    rp = mid - 1
    
print(res)