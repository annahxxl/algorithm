n = int(input())
cnt = list(map(int, input().split()))

seq = [0] * n # 원 수열

for i in range(n):
  for j in range(n):
    if cnt[i]==0 and seq[j]==0:
      seq[j] = i+1
      break
    elif seq[j] == 0:
      cnt[i] -= 1
      
for x in seq:
  print(x, end=' ')