def DFS(x):
  if x > 0:
    # print(x, end=' ') # 3 2 1 출력
    # DFS(x-1)
    DFS(x-1)
    print(x, end=' ') # 1 2 3 출력
    
if __name__ == '__main__':
  n = int(input())
  DFS(n)