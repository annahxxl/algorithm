n = int(input())
cnt = 0

for num in range(2, n+1):
  for i in range(2, num):
    if num % i == 0:
      break
  else:
    cnt += 1
      
print(cnt)

# 제한 시간 초과 😥