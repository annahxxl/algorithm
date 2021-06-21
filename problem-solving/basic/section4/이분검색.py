n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
lp = 0 # 왼쪽 포인터 (index)
rp = n-1 # 오른쪽 포인터 (index)

while lp <= rp:
  mid = (lp+rp) // 2
  if nums[mid] == m:
    print(mid+1)
    break
  elif nums[mid] > m:
    rp = mid - 1
  else:
    lp = mid + 1