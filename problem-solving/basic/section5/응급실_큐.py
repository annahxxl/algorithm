from collections import deque

n, m = map(int, input().split())
p = deque([(pos, val) for pos, val in enumerate(list(map(int, input().split())))]) # 순서와 위험도 tuple로 저장
cnt = 0 # m번째 환자의 진료 받는 순서

while p:
  cur = p.popleft() # 현재 대기목록 첫 번째 환자
  if any(cur[1] < x[1] for x in p): # 위험도 비교
    p.append(cur)
  else:
    cnt += 1
    if cur[0] == m:
      print(cnt)
      break