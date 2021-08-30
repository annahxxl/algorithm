def Count(capacity): # DVD 개수 구하기
  cnt = 1
  SUM = 0
  for i in music:
    if SUM + i > capacity:
      cnt += 1
      SUM = i
    else:
      SUM += i
  return cnt
  
n, m = map(int, input().split())
music = list(map(int, input().split())) # 노래 길이
lp = max(music)
rp = sum(music)
while lp <= rp: # 최소 용량 크기 구하기
  mid = (lp + rp) // 2
  if Count(mid) <= m:
    res = mid
    rp = mid - 1
  else:
    lp = mid + 1
print(res)