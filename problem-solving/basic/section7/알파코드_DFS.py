def DFS(code_idx, res_idx):
  global cnt
  if code_idx == n:
    cnt += 1
    for i in range(res_idx):
      print(chr(res[i] + 64), end='')
    print()
  else:
    for i in range(1, 27):
      if code[code_idx] == i:
        res[res_idx] = i
        DFS(code_idx + 1, res_idx + 1)
      elif i >= 10 and code[code_idx] == i // 10 and code[code_idx + 1] == i % 10:
        res[res_idx] = i
        DFS(code_idx + 2, res_idx + 1)

if __name__ == '__main__':
  code = list(map(int, input()))
  n = len(code)
  res = [0] * n
  cnt = 0
  code.append(-1) # 13 라인에서 에러(list index out of range) 피하기 위해 추가
  DFS(0, 0)
  print(cnt)