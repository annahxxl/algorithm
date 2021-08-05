t = int(input())
for i in range(t):
  n, s, e, k = map(int, input().split())
  nums = list(map(int, input().split()))
  nums = sorted(nums[s-1 : e])
  print("#%d %d" %(i+1, nums[k-1]))