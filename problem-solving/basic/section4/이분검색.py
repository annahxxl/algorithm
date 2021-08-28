n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lp = 0
rp = n - 1
while lp <= rp:
  mid = (lp + rp) // 2
  if m == nums[mid]:
    print(mid + 1)
    break
  elif m < nums[mid]:
    rp = mid - 1
  elif m > nums[mid]:
    lp = mid + 1