# 소수를 구하는 여러 방법 중
# '에라토스테네스의 체'는 가장 대표적인 소수 판별 알고리즘
# 소수를 대량으로 빠르고 정확하게 구하는 방법

n = int(input())
ch = [0] * (n+1) # index값 == 판별해야하는 숫자
cnt = 0

for num in range(2, n+1):
  if ch[num] == 0:
    cnt += 1
    for i in range(num, n+1, num): # range(start, end+1[, step]), num의 배수 걸러내기
      ch[i] = 1
      
print(cnt)