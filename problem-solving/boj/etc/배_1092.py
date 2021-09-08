n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
cranes.sort(reverse=True)
boxes.sort(reverse=True)
if cranes[0] < boxes[0]:
  print(-1)
else:
  positions = [0] * n # 체크해야할 박스 시작 index
  checked = [False] * m # 각 박스를 옮겼는지의 여부
  cnt = 0
  res = 0
  while True:
    if cnt == m:
      break
    for i in range(n):
      while positions[i] < m:
        if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
          checked[positions[i]] = True
          positions[i] += 1
          cnt += 1
          break
        positions[i] += 1
    res += 1
  print(res)