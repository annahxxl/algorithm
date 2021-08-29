# 이분검색을 이용한 결정알고리즘을 사용하여 풀 수 있는 문제 특징:
# 특정 범위 안에 답이 있다는 것을 알 수 있을 경우

def Count(length):
  cnt = 0
  for line in lines:
    cnt += (line // length)
  return cnt

k, n = map(int, input().split())
lines = sorted([int(input()) for _ in range(k)])
MAX = max(lines)
lp = 1
rp = MAX
while lp <= rp:
  mid = (lp + rp) // 2
  if Count(mid) >= n:
    result = mid
    lp = mid + 1
  else:
    rp = mid - 1
print(result)