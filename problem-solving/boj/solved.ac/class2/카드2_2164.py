# 시간 초과
# import sys
# n = int(sys.stdin.readline())
# cards = [i+1 for i in range(n)]
# for _ in range(len(cards)):
#   cards.pop(0)
#   cards.append(cards.pop(0))
#   if len(cards) == 1:
#     print(cards[0])
#     break

# deque 사용
# deque(덱)은 스택이나 큐의 기능 모두 포함, 자료의 입력과 출력을 양 쪽 끝에서 가능하게 하는 자료구조
from collections import deque
n = int(input())
cards = deque(list(range(1, n+1)))
while len(cards) > 1:
  cards.popleft()
  cards.append(cards.popleft())
print(cards[0])