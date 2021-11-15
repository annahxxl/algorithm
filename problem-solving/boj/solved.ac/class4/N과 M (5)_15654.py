def DFS(idx):
  if idx == m:
    for x in seq:
      print(x, end=' ')
    print()
  else:
    for i in range(n):
      if not used[i]:
        seq[idx] = nums[i]
        used[i] = True
        DFS(idx+1)
        used[i] = False

if __name__ == '__main__':
  n, m = map(int, input().split())
  nums = list(map(int, input().split()))
  seq = [0] * m
  used = [False] * n # 사용한 숫자의 idx를 체크하는 리스트
  nums.sort()
  DFS(0)