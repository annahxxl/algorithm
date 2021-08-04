t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  queue = list(map(int, input().split()))
  idx_que = [i for i in range(n)]
  target_idx = m
  cnt = 0
  while queue:
    if max(queue) == queue[0]:
      cnt += 1
      queue.pop(0)
      if idx_que.pop(0) == m:
        print(cnt)
    else:
      queue.append(queue.pop(0))
      idx_que.append(idx_que.pop(0))
      
'''
* enumerate: 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
  print(p)
-------------------------
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  queue = list(map(int, input().split()))
  queue = [(i, idx) for idx, i in enumerate(queue)]
  cnt = 0
  while True:
    if max(queue, key=lambda x: x[0])[0] == queue[0][0]:
      cnt += 1
      if queue[0][1] == m:
        print(cnt)
        break
      else:
        queue.pop(0)
    else:
      queue.append(queue.pop(0))
'''