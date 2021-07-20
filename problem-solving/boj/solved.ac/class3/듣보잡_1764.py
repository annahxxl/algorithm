# 시간 초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# not_heard, not_seen = list(), list()
# for _ in range(n):
#   not_heard.append(input().strip())
# for _ in range(m):
#   not_seen.append(input().strip())
# cnt = 0
# result = list()
# for p in not_heard:
#   if p in not_seen:
#     cnt += 1
#     result.append(p)
# print(cnt)
# result.sort()
# for p in result:
#   print(p)

# 집합
n, m = map(int, input().split())
not_heard, not_seen = set(), set()
for _ in range(n):
  not_heard.add(input())
for _ in range(m):
  not_seen.add(input())
result = sorted(list(not_heard&not_seen))
print(len(result))
for i in result:
  print(i)