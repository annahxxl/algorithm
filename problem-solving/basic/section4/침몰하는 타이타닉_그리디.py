n, m = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()

cnt = 0

# while weight:
#   if len(weight) == 1:
#     cnt += 1
#     break
#   if weight[0]+weight[-1] > m:
#     weight.pop()
#     cnt += 1
#   else:
#     weight.pop(0)
#     weight.pop()
#     cnt += 1
    
# sol2 - 덱(deque) 자료구조 사용
# list에서 pop 사용 시 뒤의 자료들이 앞으로 당겨지는 연산을 함
# 반면에 덱(deque) 자료구조는 자료들이 움직이지 않음
from collections import deque

weight = deque(weight)
    
while weight:
  if len(weight) == 1:
    cnt += 1
    break
  if weight[0]+weight[-1] > m:
    weight.pop()
    cnt += 1
  else:
    weight.popleft()
    weight.pop()
    cnt += 1

print(cnt)