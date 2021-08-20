'''
# my solution: O(NlogN)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
result = sorted(a + b)
for i in result:
  print(i, end=' ')
'''

# other solution (병합 정렬): O(N)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ap, bp = 0, 0 # 포인터
result = list()
while ap < len(a) and bp < len(b):
  if a[ap] < b[bp]:
    result.append(a[ap])
    ap += 1
  else:
    result.append(b[bp])
    bp += 1
if ap == len(a):
  result += b[bp:]
elif bp == len(b):
  result += a[ap:]
for i in result:
  print(i, end=' ')