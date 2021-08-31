def Count(distance): # 말을 넣을 수 있는 개수
  cnt = 1
  ep = loc[0] # 현재 마지막으로 말을 넣은 지점
  for i in range(1, n):
    if loc[i] - ep >= distance:
      cnt += 1
      ep = loc[i]
  return cnt

n, c = map(int, input().split())
loc = [int(input()) for _ in range(n)]
lp = 0
rp = loc[n-1]
loc.sort()
while lp <= rp:
  mid = (lp + rp) // 2 # 간격
  if Count(mid) >= c:
    result = mid
    lp = mid + 1
  else:
    rp = mid - 1
print(result)