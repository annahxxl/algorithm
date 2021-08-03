'''
# my solution
n, k = map(int, input().split())
nums = []
for i in range(1, n+1):
  if n % i == 0:
    nums.append(i)
nums.sort()
if k > len(nums):
  print(-1)
else:
  print(nums[k-1])
'''

# other solution
n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
  if n % i == 0:
    cnt += 1
  if cnt == k:
    print(i)
    break
else: # for문이 정상적으로 종료 시 실행
  print(-1)