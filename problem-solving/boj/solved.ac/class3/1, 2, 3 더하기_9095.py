# t = int(input())
# def sol(n):
#   if n == 1:
#     return 1
#   elif n == 2:
#     return 2
#   elif n == 3:
#     return 4
#   return sol(n-1) + sol(n-2) + sol(n-3)
# for _ in range(t):
#   n = int(input())
#   print(sol(n))

t = int(input())
for _ in range(t):
  n = int(input())
  cnt = [0, 1, 2, 4]
  for i in range(4, n+1):
    cnt.append(cnt[i-1] + cnt[i-2] + cnt[i-3])
  print(cnt[n])