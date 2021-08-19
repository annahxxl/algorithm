'''
# my solution
s = input()
num = list()
for i in s:
  if i.isdigit():
    num.append(i)
num = int(''.join(num))
print(num)
cnt = 0
for i in range(1, num+1):
  if num % i == 0:
    cnt += 1
print(cnt)
'''

# other solution
s = input()
res = 0
for i in s:
  if i.isdecimal():
    res = res * 10 + int(i)
print(res)
cnt = 0
for i in range(1, res+1):
  if res % i == 0:
    cnt += 1
print(cnt)