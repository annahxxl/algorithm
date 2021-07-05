n, m = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

result = 0

for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    for k in range(j+1, len(nums)):
      sum = nums[i] + nums[j] + nums[k]
      if sum <= m:
        result = max(result, sum)
        
print(result)