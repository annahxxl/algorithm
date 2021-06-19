str = input()
digit = []
cnt = 0 # 약수의 개수

for i in str:
  if i.isdigit():
    digit.append(i)
    
digit = int(''.join(digit))

print(digit)

for i in range(1, digit+1):
  if digit % i == 0:
    cnt += 1

print(cnt)