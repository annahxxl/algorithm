'''
# my solution (시간 초과)
def DFS(idx, SUM):
  global MAX
  if idx == n:
    if SUM <= c and SUM > MAX:
      MAX = SUM
  else: 
    DFS(idx+1, SUM+weight[idx]) # weight[idx]를 포함하는 경우
    DFS(idx+1, SUM) # # weight[idx]를 포함하지 않는 경우

if __name__ == '__main__':
  c, n = map(int, input().split())
  weight = [int(input()) for _ in range(n)]
  MAX = -1 
  DFS(0, 0)
  print(MAX)
'''

# solution
def DFS(idx, SUM, tsum):
  global MAX
  if SUM + (total - tsum) < MAX:
    return
  if SUM > c:
    return
  if idx == n:
    if SUM > MAX:
      MAX = SUM
  else: 
    DFS(idx+1, SUM + weight[idx], tsum + weight[idx]) # weight[idx]를 포함하는 경우
    DFS(idx+1, SUM, tsum + weight[idx]) # # weight[idx]를 포함하지 않는 경우

if __name__ == '__main__':
  c, n = map(int, input().split())
  weight = [int(input()) for _ in range(n)]
  MAX = -1
  total = sum(weight)
  DFS(0, 0, 0)
  print(MAX)