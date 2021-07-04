def DFS(node):
  if node > 7:
    return
  else:
    print(node, end=' ') # 전위순회 출력 : 1 2 4 5 3 6 7
    DFS(node*2)
    # print(node, end=' ') # 중위순회 출력 : 4 2 5 1 6 3 7
    DFS(node*2+1)
    # print(node, end=' ') # 후위순회 출력 : 4 5 2 6 7 3 1

if __name__ == "__main__":
  DFS(1)