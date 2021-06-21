n, m = map(int, input().split())
music = list(map(int, input().split()))

def count(capacity): # DVD 개수 구하기
  cnt = 1
  sum = 0
  for i in music:
    if sum+i > capacity:
      cnt += 1
      sum = i
    else:
      sum += i
  return cnt

lp = max(music)
rp = sum(music)
res = 0

while lp <= rp:
  mid = (lp+rp) // 2
  if count(mid) <= m:
    res = mid
    rp = mid - 1
  else:
    lp = mid + 1
    
print(res)