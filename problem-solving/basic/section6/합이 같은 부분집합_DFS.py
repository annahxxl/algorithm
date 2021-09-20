import sys

def DFS(idx, SUM):
  if SUM > total // 2:
    return
  if idx == n:
    if SUM == total - SUM:
      print('YES')
      sys.exit()
  else:
    DFS(idx+1, SUM+nums[idx]) # nums[idx]를 포함하는 경우
    DFS(idx+1, SUM) # nums[idx]를 포함하지 않는 경우

if __name__ == '__main__':
  n = int(input())
  nums = list(map(int, input().split()))
  total = sum(nums)
  DFS(0, 0)
  print('NO')