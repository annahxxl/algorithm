'''
# solution 1
def DFS(idx, start_idx):
    global cnt
    if idx == k:
      if sum(res) % m == 0:
        cnt += 1
    else:
        for i in range(start_idx, n):
            res[idx] = num[i]
            DFS(idx + 1, i + 1)

if __name__ == "__main__":
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    res = [0] * k
    DFS(0, 0)
    print(cnt)
'''

# solution 2
def DFS(idx, start_idx, SUM):
  global cnt
  if idx == k:
    if SUM % m == 0:
      cnt += 1
  else:
    for i in range(start_idx, n):
      DFS(idx + 1, i + 1, SUM + nums[i])

if __name__ == '__main__':
  n, k = map(int, input().split())
  nums = list(map(int, input().split()))
  m = int(input())
  cnt = 0
  DFS(0, 0, 0)
  print(cnt)