n, m = map(int, input().split())
nums = list(map(int, input().split()))

lp = 0 # left pointer
rp = 1 # right pointer
tot = nums[0] # nums[lp] 부터 nums[rp] 직전 값의 합
cnt = 0

while True:
  if tot < m:
    if rp < n:
      tot += nums[rp]
      rp += 1
    else: # rp = n
      break
  elif tot == m:
    cnt += 1
    tot -= nums[lp]
    lp += 1
  else:
    tot -= nums[lp]
    lp += 1
    
print(cnt)