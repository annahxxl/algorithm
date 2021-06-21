k, n = map(int, input().split())
line = []
res = 0
largest = 0 # 가장 긴 랜선

for _ in range(k):
  tmp = int(input())
  line.append(tmp)
  largest = max(largest, tmp)
  
def count(len): # 만들어진 랜선 개수 구하기
  cnt = 0
  for i in line:
    cnt += (i//len)
  return cnt

# 이분 검색
lp = 1
rp = largest

while lp <= rp:
  mid = (lp+rp) // 2
  if count(mid) >= n:
    res = mid
    lp = mid + 1
  else:
    rp = mid - 1
    
print(res)