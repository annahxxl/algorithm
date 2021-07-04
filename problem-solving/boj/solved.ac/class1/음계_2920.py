nums = list(map(int, input().split(' ')))

ascending = True
descending = True

for i in range(1, 8):
  if nums[i] > nums[i-1]:
    descending = False
  elif nums[i] < nums[i-1]:
    ascending = False
    
if ascending:
  print('ascending')
elif descending:
  print('descending')
else:
  print('mixed')